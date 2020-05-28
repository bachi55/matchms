from .Scores import Scores
from .typing import SimilarityFunction, ReferencesType, QueriesType


def calculate_scores(references: ReferencesType,
                     queries: QueriesType,
                     similarity_function: SimilarityFunction) -> Scores:
    """Calculate the similarity between all reference objects versus all query objects.

    Example to calculate scores between 2 spectrums and iterate over the scores

    .. testcode::

        import numpy as np
        from matchms import calculate_scores, Spectrum
        from matchms.similarity import CosineGreedy

        spectrum_1 = Spectrum(mz=np.array([100, 150, 200.]),
                              intensities=np.array([0.7, 0.2, 0.1]),
                              metadata={'id': 'spectrum1'})
        spectrum_2 = Spectrum(mz=np.array([100, 140, 190.]),
                              intensities=np.array([0.4, 0.2, 0.1]),
                              metadata={'id': 'spectrum2'})
        spectrums = [spectrum_1, spectrum_2]

        scores = calculate_scores(spectrums, spectrums, CosineGreedy())

        for (reference, query, score, n_matching) in scores:
            print(f"Cosine score between {reference.metadata['id']} and {query.metadata['id']}" +
                  f" is {score:.2f} with {n_matching} matched peaks")

    Should output

    .. testoutput::

        Cosine score between spectrum1 and spectrum1 is 1.00 with 3 matched peaks
        Cosine score between spectrum1 and spectrum2 is 0.52 with 1 matched peaks
        Cosine score between spectrum2 and spectrum1 is 0.52 with 1 matched peaks
        Cosine score between spectrum2 and spectrum2 is 1.00 with 3 matched peaks

    Parameters
    ----------
    references
        List of reference objects
    queries
        List of query objects
    similarity_function
        Function which accepts a reference + query object and returns a score or tuple of scores

    Returns
    -------

    Scores
    """

    return Scores(references=references,
                  queries=queries,
                  similarity_function=similarity_function).calculate()
