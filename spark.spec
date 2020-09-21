
Summary: A unified analytics engine for large-scale data processing.
Name: spark
Version: 3.0.1
Release: 1.0
License: Apache License v2.0
URL: http://spark.apache.org/
BuildArch: noarch
Source0: https://github.com/apache/spark/archive/v%{version}.tar.gz

BuildRequires: java-1.8.0-openjdk-devel, maven
#BuildRequires: maven

Requires: java-1.8.0-openjdk

ExclusiveArch: x86_64 aarch64

%description
Apache Spark achieves high performance for both batch and streaming data, using a state-of-the-art DAG scheduler, a query optimizer, and a physical execution engine.

%prep
%setup -q

%build
mvn -DskipTests clean package

%install
mkdir -p %{buildroot}/opt/%{name}-${version}/

%filess
/opt/%{name}-${version}/*


%changelog
* Fri Sep 18 2020 Hubble_Zhu<hubble_zhu@qq.com> - 1.0
- Init package


