# fanza_dojin_exporter
FANZA で買った同人(ゲーム|CG集)などの購入物一覧を json に出力するヤツ

# require

* python
* selenium package

# usage

途中、手動で頑張ります :-)

```
# ipython

import selenium.webdriver
import fanza_ero

wd = selenium.webdriver.Chrome()

# <手動で頑張る>
# 1. 開いたブラウザ上で、購入物一覧ページ (https://www.dmm.co.jp/dc/-/mylibrary/) に飛びます
# 2. 左にある "購入済み作品" の scroll bar を下に下げきります。 つまり、購入物一覧を全て load します
# </手動で頑張る>

jsonString = fanza_ero.export(wd)
```

