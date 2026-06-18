import requests, socket

class HealthChecker:
    def http(self, url, expected=200, timeout=5):
        try: r = requests.get(url, timeout=timeout); return {"url": url, "ok": r.status_code==expected}
        except Exception as e: return {"url": url, "ok": False, "error": str(e)}
    def tcp(self, host, port, timeout=5):
        try: s=socket.create_connection((host,port),timeout=timeout); s.close(); return {"host":host,"ok":True}
        except: return {"host":host,"ok":False}
