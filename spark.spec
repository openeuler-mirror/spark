%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global debug_package %{nil}

Summary: A unified analytics engine for large-scale data processing.
Name: spark
Version: 3.2.0
Release: 1.2
License: Apache License v2.0
URL: http://spark.apache.org/
Source0: https://github.com/apache/spark/archive/v%{version}.tar.gz
Source1: settings.xml

Patch0001: 0001-modify-maven-version-for-3.6.3-to-3.5.4.patch

BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: maven

Requires: java-1.8.0-openjdk

ExclusiveArch: x86_64 aarch64

%description
Apache Spark achieves high performance for both batch and streaming data, using a state-of-the-art DAG scheduler, a query optimizer, and a physical execution engine.

%prep
%setup -q

%patch0001 -p1

%build
cp %{SOURCE1} ./settings.xml
mvn -DskipTests clean package -s settings.xml

%install
mkdir -p %{buildroot}/opt/
cp -rf ../%{name}-%{version} %{buildroot}/opt/apache-%{name}-%{version}

%files
/opt/apache-%{name}-%{version}


%changelog
* Fri Nov 12 2021 Wuzeyiii<wuzeyi1@huawei.com> - 1.2
- Update spark version

* Fri Sep 18 2020 Hubble_Zhu<hubble_zhu@qq.com> - 1.0
- Init package

