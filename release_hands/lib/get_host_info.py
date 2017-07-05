import requests
import json


def get_webapi_json(host,url):
    query_url = 'http://%s%s'%(host,url)
    response = requests.get(query_url)
    return json.loads(response.text)

def get_opcenter_items():
    '''
    get cluster name
    :param env: 环境 production or ab
    :return:dict_keys(['lf_weixin', 'mjq_app', 'lf_qq', 'mjq_qq', 'lf_coupon', 'lf_app', 'lf_pc', 'mjq_coupon', 'mjq_pc', 'mjq_weixin', 'jos'])
    '''
    clusters = get_webapi_json('opcenter.jd.com', '/group/api/clusters/')
    production_clusters = clusters['CLUSTERMAP_HOSTS']['production'].keys()
    ab_cluster = clusters['CLUSTERMAP_HOSTS']['ab'].keys()
    return {
        'production': production_clusters,
        'ab': ab_cluster,
    }


def get_opcenter_hosts(env,clusters):
    '''
    get host
    :param env: 环境 production or ab
    :param clusters:
    :return:
    '''
    host_list=list()
    for cluster in clusters:
        url = '/api/cluster/info/?&cluster=%s-%s' % (env, cluster)
        info = get_webapi_json('opcenter.jd.com', url)
        apps = info['nodes'].keys()
        #dict_keys(['searcher_p4', 'dmerger', 'searcher_p1', 'detail', 'searcher_p3', 'searcher_p0', 'blender', 'searcher_p2', 'smerger'])
        for app_name in  apps:
            group = '[%s-%s-%s]' % (
                env,
                cluster,
                app_name,)
            host_list.append({group:[ host['ip'] for host in info['nodes'][app_name]]})
    return host_list


def create_ansible_hosts(ansible_hosts, path ):
    #Create a file named hosts for ansilbe
    with open(path,'w',encoding='utf-8') as file:
        for info in ansible_hosts:
            for cluster,ips in info.items():
                file.writelines((cluster,'\n'))
                for ip in ips:
                    file.writelines((ip,'\n'))

def get_result():
    opcenter_items=get_opcenter_items()
    production_hosts = get_opcenter_hosts('production', opcenter_items['production'])
    ab_hosts = get_opcenter_hosts('ab', opcenter_items['ab'])
    ansible_hosts = list()
    ansible_hosts.extend(production_hosts)
    ansible_hosts.extend(ab_hosts)

    #Create a file for ansible
    create_ansible_hosts(ansible_hosts,'hosts.txt')

if __name__ == '__main__':
    get_result()