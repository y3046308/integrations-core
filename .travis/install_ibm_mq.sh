#!/bin/bash

set -ex

TMP_DIR=/tmp/mq
MQ_URL=https://public.dhe.ibm.com/ibmdl/export/pub/software/websphere/messaging/mqadv/mqadv_dev910_linux_x86-64.tar.gz
MQ_PACKAGES="MQSeriesRuntime-*.rpm MQSeriesServer-*.rpm MQSeriesMsg*.rpm MQSeriesJava*.rpm MQSeriesJRE*.rpm MQSeriesGSKit*.rpm"

apt-get update
apt-get install -y --no-install-recommends \
  bash \
  bc \
  coreutils \
  curl \
  debianutils \
  findutils \
  gawk \
  grep \
  libc-bin \
  mount \
  passwd \
  procps \
  rpm \
  sed \
  tar \
  util-linux

mkdir -p $TMP_DIR
pushd $TMP_DIR
  curl -LO $MQ_URL
  tar -zxvf ./*.tar.gz
  pushd MQServer
    ./mqlicense.sh -text_only -accept
    rpm -ivh --force-debian $MQ_PACKAGES
    /opt/mqm/bin/setmqinst -p /opt/mqm -i
  popd
popd

set +ex
