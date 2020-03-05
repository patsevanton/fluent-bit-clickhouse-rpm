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
ls
cd build
ls
cp fluent-bit-clickhouse ../../../../../../fluent-bit-clickhouse

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 fluent-bit-clickhouse %{buildroot}%{_bindir}/fluent-bit-clickhouse
install -d %{buildroot}/etc/fluent-bit-clickhouse

#%pre
#/usr/bin/getent group fluent-bit-clickhouse > /dev/null || /usr/sbin/groupadd -r fluent-bit-clickhouse
#/usr/bin/getent passwd fluent-bit-clickhouse > /dev/null || /usr/sbin/useradd -r -d /usr/lib/fluent-bit-clickhouse -s /bin/bash -g fluent-bit-clickhouse fluent-bit-clickhouse

%files
#%defattr(-,fluent-bit-clickhouse,fluent-bit-clickhouse,-)
%{_bindir}/fluent-bit-clickhouse
/etc/fluent-bit-clickhouse/config.yaml
