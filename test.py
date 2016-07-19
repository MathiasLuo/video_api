from common.util import getJsonByUrl

ca = getJsonByUrl("http://v.youku.com/v_show/id_XMTY0NzYwMjg0OA==.html?from=y1.3-idx-beta-1519-23042.223465.1-1")
for key in ca.keys():
    print(len(ca[key]))
