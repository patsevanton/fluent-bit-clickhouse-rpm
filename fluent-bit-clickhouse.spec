Name:          fluent-bit-clickhouse
Version:       0.2
Release:       1
Summary:       fluent-bit-clickhouse
License:       ASL 2.0
Source0:       build.sh
BuildRequires: golang
BuildRequires: make
BuildRequires: tree
Requires(pre): /usr/sbin/useradd, /usr/bin/getent
Requires(postun): /usr/sbin/userdel

%description
fluent-bit-clickhouse

%build
export GOPATH=%{_builddir}/_build
echo $GOPATH
mkdir -p $GOPATH/src/github.com/iyacontrol/
git clone https://github.com/iyacontrol/fluent-bit-clickhouse.git $GOPATH/src/github.com/iyacontrol/fluent-bit-clickhouse
cd $GOPATH/src/github.com/iyacontrol/fluent-bit-clickhouse
ls $GOPATH/src/github.com/iyacontrol/fluent-bit-clickhouse
go build -buildmode=c-shared -o clickhouse.so
cp clickhouse.so ../../../../../../../clickhouse.so
cd -
ls
pwd

%install
ls
pwd
install -d %{buildroot}/var/lib/fluent-bit/
install -p -m 0755 clickhouse.so %{buildroot}/var/lib/fluent-bit/clickhouse.so

%files
/var/lib/fluent-bit/clickhouse.so
