from celery.task import task
import logging
from dpgraph.models import Node
from providers import Machine

SPLUNK_BIN = "/tmp/splunk/bin/splunk"

logger = logging.getLogger("async_deploy_task")

@task
def initialize_master(node_id):
    '''
    initialize a node to be an index cluster master
    :param node_id: the node selected to be the index master
    :return:
    '''
    node = Node.objects.get(pk=int(node_id))
    machine = Machine(node)

    return_code = 0
    if (machine.is_ssh_accessible()):
        command = "{s} {args}".format(
            s=SPLUNK_BIN,
            args=("edit cluster-config -mode master -secret secret12 "
                  "-auth admin:notchangeme"))
        _, tmp_return_code = machine.execute_command(command)
        return_code += tmp_return_code

        command = "{s} {args}".format(s=SPLUNK_BIN, args="stop -f")
        _, tmp_return_code = machine.execute_command(command)
        return_code += tmp_return_code
        if return_code > 0:
            raise Exception("Command execute failed.")
    else:
        raise Exception("Machine is unreachable.")

@task
def connect_to_index_cluster(node_id, master_id):
    '''
    add a node to an index cluster, since master
    :param node_id:  should be indexer, searchhead
    :param master_id: the index cluster master
    :return:
    '''
    pass

@task
def disconnect_from_index_cluster(node_id):
    '''
    remove a node from an index cluster, here just remove the config on that node,
    so no need to know master
    :param node_id: the node to be removed from index cluster
    :return:
    '''
    pass

@task
def initialize_license_master(node_id):
    '''
    initialize a node to be a license master
    :param node_id: the node selected to be the license master
    :return:
    '''
    pass

@task
def connect_to_license_master(node_id, master_id):
    '''
    connect to a license master
    :param node_id: the node needs to connect to a license master
    :param master_id: the license master
    :return:
    '''
    pass

@task
def disconnect_from_license_master(node_id):
    '''
    disconnect from a license master here just remove the config on that node,
    so no need to know master
    :param node_id: the node needs to disconnect from a license master
    :return:
    '''
    pass

@task
def initialize_deployer(node_id):
    '''
    Initialize a node to be a deployer
    :param node_id: the node to be a deployer
    :return:
    '''
    pass

@task
def initialize_sh(sh_id, deployer_id):
    '''
    Initialize a search head, this includes connect to a deployer
    :param sh_id:
    :param deployer_id:
    :return:
    '''
    pass

@task
def bootstrap_shc_captain(sh_id):
    '''
    Bootstrap a search head cluster captain
    :param sh_id: the search head to be captain
    :return:
    '''
    pass

@task
def add_search_peer(peer_id):
    '''
    Add a node as a search peer
    :param peer_id: the search peer node to be added
    :return:
    '''
    pass

@task
def remove_search_peer(peer_id):
    '''
    Remove a search peer
    :param peer_id: the search peer node to be removed
    :return:
    '''
    pass