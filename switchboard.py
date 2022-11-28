from texasbbq import main, GitSource, GitTarget


class ScikitLearnSource(GitSource):

    module = __name__

    @property
    def name(self):
        return "scikit-learn"

    @property
    def clone_url(self):
        return "https://github.com/scikit-learn/scikit-learn"

    @property
    def git_ref(self):
        return "main"

    @property
    def conda_dependencies(self):
        return ["-c conda-forge numpy scipy threadpoolctl joblib"]

    @property
    def install_command(self):
        return (
            "pip install --pre --extra-index "
            "https://pypi.anaconda.org/scipy-wheels-nightly/simple scikit-learn"
        )


class ImbalanceLearnTests(GitTarget):
    @property
    def name(self):
        return "imbalanced-learn"

    @property
    def clone_url(self):
        return "https://github.com/scikit-learn-contrib/imbalanced-learn"

    @property
    def git_ref(self):
        return "main"

    @property
    def install_command(self):
        return "pip install ."

    @property
    def test_command(self):
        return "pytest -v imblearn"

    @property
    def conda_dependencies(self):
        return ["pytest"]


if __name__ == "__main__":
    main(ScikitLearnSource())
