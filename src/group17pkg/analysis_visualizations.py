import matplotlib.pyplot as plt


def visualize_classification(data, preds):
    """
    Produces a scatteplot with the classified data points for the given dataset. The scatterplot has 
    TSH concentration on the x-axis and TT4 concentration on the y-axis, with points coloured by
    the prediction 

    Parameters
    -------
    data: pd.DataFrame:
        The dataset the predictions are taken from. 
    preds: pd.DataFrame:
         The classification predictions that have been produced. Should contain labels of P or N for
         each row in the dataframe

    Returns
    -------
    fig: Scatterplot object visualizing the classifications of the data points

    Example
    -------
    Produce a scatterplot analyzing the classification of hyperthyroid disease
    >>> import group17pkg as grp
        Inputting the dataframe along with the prediction set to use visualize_classification
    >>> grp.visualiaze_classification(hyper_train, train_preds)
        This will produce a scatterplot visualizing the predictions for the hyper_train dataset. 
    """
    fig = plt.figure()
    plt.scatter(data["TSH"], data["TT4"], c=preds, s=50, cmap='viridis')
    plt.xlabel("TSH concentration")
    plt.ylabel("TT4 concentration")
    return fig
