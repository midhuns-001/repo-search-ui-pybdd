import pytest

pytest.main([
    '--driver=chrome',
    '--driver-path=./drivers/chromedriver',
    '-m=t1'
])