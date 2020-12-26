# -*- coding: utf-8 -*-
from typing import List


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    # 实现用例反转执行
    # items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')