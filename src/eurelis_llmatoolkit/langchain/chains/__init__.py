from langchain.chains.base import Chain

from eurelis_llmatoolkit.utils.base_factory import ProviderFactory


class GenericChainsFactory(ProviderFactory[Chain]):
    """
    Generic chains factory, provide with a conversational with memory question oriented chain
    """

    ALLOWED_PROVIDERS = {
        "conversational-retrieval": "eurelis_llmatoolkit.langchain.chains.conversational_retrieval.ConversationalRetrievalChainFactory",
    }

    def __init__(self):
        super().__init__()
        # we provide a default value for provider parameter
        self.params["provider"] = "conversational-retrieval"
