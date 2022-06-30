import requests
URL = "https://simak.unsil.ac.id/us-unsil/baa/transkripmhsw.php?gos=_CetakTranskrip&MhswID=197002059&_rnd=zrH5qdg1&jen=2"
response = requests.get(URL)
open("instagram.ico", "wb").write(response.content)