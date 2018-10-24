class NanpreException(Exception):
    """ルート例外"""


class BoardError(NanpreException):
    """`Board`クラスに関する例外"""


class SolverError(NanpreException):
    """`Solver`クラスに関する例外"""
