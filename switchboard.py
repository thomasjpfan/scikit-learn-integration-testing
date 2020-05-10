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
        return "master"

    @property
    def install_command(self):
        return "pip install -e ."

    @property
    def conda_dependencies(self):
        return []


class ImbalanceLearnTests(GitTarget):
    @property
    def name(self):
        return "imbalanced-learn"

    @property
    def clone_url(self):
        return "https://github.com/scikit-learn-contrib/imbalanced-learn"

    @property
    def git_ref(self):
        return "master"

    @property
    def install_command(self):
        return "pip install -e ."

    @property
    def test_command(self):
        return "pytest -v imblearn"

    @property
    def conda_dependencies(self):
        return ["pytest"]


class ShapTests(GitTarget):
    @property
    def name(self):
        return "shap"

    @property
    def clone_url(self):
        return "https://github.com/slundberg/shap"

    @property
    def git_ref(self):
        return "master"

    @property
    def install_command(self):
        return "pip install -e ."

    @property
    def test_command(self):
        return "python setup.py nosetests"

    @property
    def conda_dependencies(self):
        return ["nose"]


if __name__ == "__main__":
    main(ScikitLearnSource())
