import requests
# from Mtool.ahrefs.models import AhrefsRank
import json
from .models import AhrefsRank, AhrefsBacklinks
REMOTE_API_URL = "http://apiv2.ahrefs.com"

class AhrefsData():
    def get_ahrefs_rank():
        headers = {'content-type': 'application/json'}
        payload = {
            'token' : "",
            'from' : "ahrefs_rank",
            'target' : "ahrefs.com",
            'mode' : "domain",
            'limit' : "2",
            # 'order_by' : "ahrefs_rank",
            'output': "json"
        }
        l = requests.get(REMOTE_API_URL, params=payload, headers=headers)
        response_dict = l.json()

        pages = response_dict['pages']
        for page in pages:
            url = page['url']
            ahrefs_rank = page['ahrefs_rank']

            AhrefsRank.objects.create(url=url, ahrefs_rank=ahrefs_rank)
        return pages

    def get_ahrefs_backlinks():
        headers = {'content-type': 'application/json'}
        payload = {
            'token' : "",
            'from' : "backlinks",
            'target' : "ahrefs.com",
            'mode' : "domain",
            'limit' : "2",
            # 'order_by' : "ahrefs_rank",
            'output': "json"
        }
        l = requests.get(REMOTE_API_URL, params=payload, headers=headers)
        response_dict = l.json()

        pages = response_dict['refpages']
        for page in pages:
            url_to = page['url_to']
            url_from = page['url_from']
            ahrefs_rank = page['ahrefs_rank']
            domain_rating = page['domain_rating']
            ip_from = page['ip_from']
            links_internal = page['links_internal']
            links_external = page['links_external']
            page_size = page['page_size']
            encoding = page['encoding']
            title = page['title']
            first_seen = page['first_seen']
            last_visited = page['last_visited']
            prev_visited = page['prev_visited']
            original = page['original']
            link_type = page['link_type']
            redirect = page['redirect']
            nofollow = page['nofollow']
            alt = page['alt']
            anchor = page['anchor']
            text_pre = page['text_pre']
            text_post = page['text_post']

            AhrefsBacklinks.objects.create(url_from=url_from, url_to=url_to, ahrefs_rank=ahrefs_rank, domain_rating=domain_rating, ip_from=ip_from,
                                      links_internal=links_internal, links_external=links_external, page_size=page_size, encoding=encoding,
                                      title=title, first_seen=first_seen, last_visited=last_visited, prev_visited=prev_visited, original=original,
                                      link_type=link_type, redirect=redirect, nofollow=nofollow, alt=alt, anchor=anchor, text_pre=text_pre,
                                      text_post=text_post)

        return pages