# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

import pymqi

QUEUE_METRICS = {
    'service_interval': pymqi.CMQC.MQIA_Q_SERVICE_INTERVAL,
    'inhibit_put': pymqi.CMQC.MQIA_INHIBIT_PUT,
    'depth_low_limit': pymqi.CMQC.MQIA_Q_DEPTH_LOW_LIMIT,
    'inhibit_get': pymqi.CMQC.MQIA_INHIBIT_GET,
    'harden_get_backout': pymqi.CMQC.MQIA_HARDEN_GET_BACKOUT,
    'service_interval_event': pymqi.CMQC.MQIA_Q_SERVICE_INTERVAL_EVENT,
    'trigger_control': pymqi.CMQC.MQIA_TRIGGER_CONTROL,
    'usage': pymqi.CMQC.MQIA_USAGE,
    'scope': pymqi.CMQC.MQIA_SCOPE,
    'type': pymqi.CMQC.MQIA_Q_TYPE,
    'depth_max': pymqi.CMQC.MQIA_MAX_Q_DEPTH,
    'backout_threshold': pymqi.CMQC.MQIA_BACKOUT_THRESHOLD,
    'depth_high_event': pymqi.CMQC.MQIA_Q_DEPTH_HIGH_EVENT,
    'depth_low_event': pymqi.CMQC.MQIA_Q_DEPTH_LOW_EVENT,
    'trigger_message_priority': pymqi.CMQC.MQIA_TRIGGER_MSG_PRIORITY,
    'depth_current': pymqi.CMQC.MQIA_CURRENT_Q_DEPTH,
    'depth_max_event': pymqi.CMQC.MQIA_Q_DEPTH_MAX_EVENT,
    'open_input_count': pymqi.CMQC.MQIA_OPEN_INPUT_COUNT,
    'persistence': pymqi.CMQC.MQIA_DEF_PERSISTENCE,
    'trigger_depth': pymqi.CMQC.MQIA_TRIGGER_DEPTH,
    'max_message_length': pymqi.CMQC.MQIA_MAX_MSG_LENGTH,
    'depth_high_limit': pymqi.CMQC.MQIA_Q_DEPTH_HIGH_LIMIT,
    'priority': pymqi.CMQC.MQIA_DEF_PRIORITY,
    'input_open_option': pymqi.CMQC.MQIA_DEF_INPUT_OPEN_OPTION,
    'message_delivery_sequence': pymqi.CMQC.MQIA_MSG_DELIVERY_SEQUENCE,
    'retention_interval': pymqi.CMQC.MQIA_RETENTION_INTERVAL,
    'open_output_count': pymqi.CMQC.MQIA_OPEN_OUTPUT_COUNT,
    'trigger_type': pymqi.CMQC.MQIA_TRIGGER_TYPE,
    'max_channels': pymqi.CMQC.MQIA_MAX_CHANNELS
}

QUEUE_MANAGER_METRICS = {
    'dist_lists': pymqi.CMQC.MQIA_DIST_LISTS,
    'max_msg_list': pymqi.CMQC.MQIA_MAX_MSG_LENGTH,
}

QUEUE_MANAGER_TAGS = {
    'QMgrIdentifier': 'MQCA_Q_MGR_IDENTIFIER',
    'ProcessName': 'MQCA_PROCESS_NAME',
}

CREATION = {
    'CreationTime': 'MQCA_CREATION_TIME',
    'CreationDate': 'MQCA_CREATION_DATE',
}


def depth_percent(queue):
    depth_current = queue.inquire(QUEUE_METRICS['depth_current'])
    depth_max = queue.inquire(QUEUE_METRICS['depth_max'])

    depth_fraction = float(depth_current) / float(depth_max)
    depth_percent = depth_fraction * 100

    return depth_percent


QUEUE_METRICS_FUNCTIONS = {
    'depth_percent': depth_percent,
}
