import httpx


def get_http_proxy():
    proxy = "socks5://openai-proxy:8388"
    return proxy


def get_http_client():
    proxy = get_http_proxy()
    http_client = httpx.AsyncClient(
        mounts={
            "http://": httpx.AsyncHTTPTransport(proxy=proxy),
            "https://": httpx.AsyncHTTPTransport(proxy=proxy),
        }
    )
    return http_client
