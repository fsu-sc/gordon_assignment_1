# Fill in the appropriate import statements from sklearn to solve the homework


class MNIST_Part1:
    def __init__(self, normalize: bool = True):
        try:
            X = np.load("mnist_X.npy")
            y = np.load("mnist_y.npy", allow_pickle=True)  # why 2nd arg required?
        except:
            print("Download MNIST data from the web")
            X, y = datasets.fetch_openml(
                "mnist_784", version=1, return_X_y=True, as_frame=False
            )

        # Save the data
        y = y.astype(np.int32)
        np.save("mnist_X.npy", X)
        np.save("mnist_y.npy", y)

        if normalize:
            X = X / X.max()

        self.X = X
        self.y = y

    def unique_elements(self):
        # Check that each class has at least 1 element in y
        classes = defaultdict(int)
        for y_val in self.y:
            classes[y_val] += 1

        print("Nb of classes: ", len(classes))

        # Not sorted
        for key in classes.keys():
            print(f"Nb elements in class {key}: {classes[key]}")

    def prepare_data(self, num_train: int = 60000, num_test: int = 10000):
        # Check in case the data is already on the computer.
        self.Xtrain, self.Xtest = (
            self.X[:num_train],
            self.X[num_train : num_train + num_test],
        )
        self.ytrain, self.ytest = (
            self.y[:num_train],
            self.y[num_train : num_train + num_test],
        )
        return self.Xtrain, self.ytrain, self.Xtest, self.ytest

    def filter_out_7_9s(self, X: NDArray[np.floating], y: NDArray[np.int32]):
        seven_nine_idx = (y == 7) | (y == 9)
        X_binary = X[seven_nine_idx, :]
        y_binary = y[seven_nine_idx]
        return X_binary, y_binary

    def train_simple_classifier_with_cv(
        self,
        X: NDArray[np.floating],
        y: NDArray[np.int32],
        clf: BaseEstimator,
        n_splits: int = 5,
        cv_class: Type[KFold] = KFold,
    ):
        cv = cv_class(n_splits=n_splits)
        scores = cross_validate(clf, X, y, cv=cv)
        return scores

    def print_cv_result_dict(self, cv_dict: Dict):
        for key, array in cv_dict.items():
            print(f"mean_{key}: {array.mean()}, std_{key}: {array.std()}")


# ----------------------------------------------------------------
class SolvePartOne(MNIST_Part1):
    def __init__(self):
        print(f"{self.__class__.__name__=}")
        print(f"{super().__class__.__bases__[0].__name__=}")  # BUG?
        super().__init__(normalize=True)
        self.Xtrain = None
        self.ytrain = None
        self.Xtest = None
        self.Ytest = None
        self.random_state = 42

        # decision gtree classifier used in part 1-C
        self.base_estimator_1C = None
        self.cross_validator_1C = None
        self.out_dict_1C = None

        self.base_estimator_1D = None
        self.cross_validator_1D = None
        self.out_dict_1D = None

        self.base_estimator_1E = None
        self.cross_validator_class_1E = None
        # dictionary of dictionaries with keys equal to the number of splits
        # Therefore: out_dict_1E[5] is a dictionary with the results of the cross_validator with 5 splits
        self.out_dict_1E = None

        self.out_dict_logistic_1F = None
        self.out_dict_svm_1F = None
        self.cross_validator_logistic_class_1F = None
        self.cross_validator_svm_class_1F = None

        # Perhaps skip 1G
        self.base_estimator_1G = None
        self.cross_validator_class_1G = None
        # Should return 'MNIST_Part1', but returns 'object'

    # test for the number of splits in the different sections since I have the cv

    def solve_assignment(self):
        """
        # Part 1-B
        """

        """
        # Part 1-C
        """

        """
        # Part 1-D
        # Decision Tree, 5-fold random permutation cross-validation
        """

        """
        # Part 1-E
        # Decision Tree, 5-fold random permutation cross-validation
        """

        """
        # Part 1F
        # Logistic Regression, 5-fold random permutation cross-validation
        """

        """
        # Part 1-G
        # Hyperparameter grid search. Don't yet know how to test
        """


if __name__ == "__main__":
    part1 = MNIST_Part1(normalize=True)
    # Xtrain, ytrain, Xtest, ytest = part1.prepare_data()

    solve_part1 = SolvePartOne()
    solve_part1.solve_assignment()
    # solve_part2()
    # solve_part3()
