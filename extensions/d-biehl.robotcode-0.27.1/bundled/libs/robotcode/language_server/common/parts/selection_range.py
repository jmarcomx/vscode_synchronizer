from __future__ import annotations

from asyncio import CancelledError
from typing import TYPE_CHECKING, Any, Final, List, Optional

from robotcode.core.async_tools import async_tasking_event, threaded
from robotcode.core.logging import LoggingDescriptor
from robotcode.jsonrpc2.protocol import rpc_method
from robotcode.language_server.common.decorators import language_id_filter
from robotcode.language_server.common.has_extend_capabilities import HasExtendCapabilities
from robotcode.language_server.common.lsp_types import (
    Position,
    SelectionRange,
    SelectionRangeOptions,
    SelectionRangeParams,
    ServerCapabilities,
    TextDocumentIdentifier,
)
from robotcode.language_server.common.text_document import TextDocument

if TYPE_CHECKING:
    from robotcode.language_server.common.protocol import LanguageServerProtocol

from .protocol_part import LanguageServerProtocolPart


class SelectionRangeProtocolPart(LanguageServerProtocolPart, HasExtendCapabilities):
    _logger: Final = LoggingDescriptor()

    def __init__(self, parent: LanguageServerProtocol) -> None:
        super().__init__(parent)

    def extend_capabilities(self, capabilities: ServerCapabilities) -> None:
        if len(self.collect):
            capabilities.selection_range_provider = SelectionRangeOptions(work_done_progress=True)

    @async_tasking_event
    async def collect(
        sender, document: TextDocument, positions: List[Position]  # NOSONAR
    ) -> Optional[List[SelectionRange]]:
        ...

    @rpc_method(name="textDocument/selectionRange", param_type=SelectionRangeParams)
    @threaded()
    async def _text_document_selection_range(
        self,
        text_document: TextDocumentIdentifier,
        positions: List[Position],
        *args: Any,
        **kwargs: Any,
    ) -> Optional[List[SelectionRange]]:
        results: List[SelectionRange] = []

        document = await self.parent.documents.get(text_document.uri)
        if document is None:
            return None

        for result in await self.collect(self, document, positions, callback_filter=language_id_filter(document)):
            if isinstance(result, BaseException):
                if not isinstance(result, CancelledError):
                    self._logger.exception(result, exc_info=result)
            else:
                if result is not None:
                    results.extend(result)

        if len(results) == 0:
            return None

        return results
