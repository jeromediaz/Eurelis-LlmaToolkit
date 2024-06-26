from typing import TYPE_CHECKING, Callable, Mapping, Sequence, TypeAlias, Union

# FIXME: Move to eurelis_llmatoolkit.langchain.types
if TYPE_CHECKING:
    from langchain.schema import Document
    from langchain.schema.embeddings import Embeddings

JSON: TypeAlias = Union[Mapping[str, "JSON"], list["JSON"], str, int, float, bool, None]
PARAMS: TypeAlias = Mapping[str, "JSON"]
FACTORY: TypeAlias = Union[str, PARAMS]
CLASS: TypeAlias = Union[str, PARAMS]

EMBEDDING: TypeAlias = Sequence[float]

DOCUMENT_MEAN_EMBEDDING: TypeAlias = Union[
    str, Callable[["Embeddings", Sequence["Document"]], EMBEDDING]
]
