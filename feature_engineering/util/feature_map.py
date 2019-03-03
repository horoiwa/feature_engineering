from .sample_data import load_df, _generate_testdf


def assign_featuretype(df, criterio=15, log=False):
    """ Assign feature types
        Parameters
        ----------
        df : DataFrame

        criterio : int
            カテゴリ変数とする基準
        
        Returns
        ----------
        feature_map : dict
    """
    feature_map = {"constant": [],
                   "binary": [],
                   "category": [],
                   "ordinal": [],
                   "numerical": []
                   }

    for col in df.columns:
        data = df[col]

        if len(set(data)) == 1:
            feature_map["constant"].append(col)
        elif len(set(data)) == 2:
            feature_map["binary"].append(col)
        elif len(set(data)) < criterio:
            try:
                [float(val) for val in data]
                feature_map["ordinal"].append(col)
            except ValueError:
                feature_map["category"].append(col)
        else:
            try:
                [float(val) for val in data]
                feature_map["numerical"].append(col)
            except ValueError:
                print("Invalid feature: {}".format(col))
                print("{} ignored".format(col))

    if log:
        print()
        print(feature_map)
        print()

    return feature_map


if __name__ == '__main__':
    df = load_df('boston')
    df = _generate_testdf(50)
    feature_map = assign_featuretype(df, log=True)
