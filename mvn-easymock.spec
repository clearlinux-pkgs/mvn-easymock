#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-easymock
Version  : 2.5
Release  : 3
URL      : https://github.com/easymock/easymock/archive/easymock-2.5.tar.gz
Source0  : https://github.com/easymock/easymock/archive/easymock-2.5.tar.gz
Source1  : https://repo1.maven.org/maven2/org/easymock/easymock-parent/3.3.1/easymock-parent-3.3.1.pom
Source2  : https://repo1.maven.org/maven2/org/easymock/easymock/2.4/easymock-2.4.jar
Source3  : https://repo1.maven.org/maven2/org/easymock/easymock/2.4/easymock-2.4.pom
Source4  : https://repo1.maven.org/maven2/org/easymock/easymock/2.5.2/easymock-2.5.2.jar
Source5  : https://repo1.maven.org/maven2/org/easymock/easymock/2.5.2/easymock-2.5.2.pom
Source6  : https://repo1.maven.org/maven2/org/easymock/easymock/3.3.1/easymock-3.3.1.jar
Source7  : https://repo1.maven.org/maven2/org/easymock/easymock/3.3.1/easymock-3.3.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: mvn-easymock-data = %{version}-%{release}
Requires: mvn-easymock-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
No detailed description available

%package data
Summary: data components for the mvn-easymock package.
Group: Data

%description data
data components for the mvn-easymock package.


%package license
Summary: license components for the mvn-easymock package.
Group: Default

%description license
license components for the mvn-easymock package.


%prep
%setup -q -n easymock-easymock-2.5

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-easymock
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-easymock/LICENSE.txt
cp src/site/License.html %{buildroot}/usr/share/package-licenses/mvn-easymock/src_site_License.html
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/easymock/easymock-parent/3.3.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/easymock/easymock-parent/3.3.1/easymock-parent-3.3.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/easymock/easymock/2.4
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/easymock/easymock/2.4/easymock-2.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/easymock/easymock/2.4
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/easymock/easymock/2.4/easymock-2.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/easymock/easymock/2.5.2
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/easymock/easymock/2.5.2/easymock-2.5.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/easymock/easymock/2.5.2
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/easymock/easymock/2.5.2/easymock-2.5.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/easymock/easymock/3.3.1
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/easymock/easymock/3.3.1/easymock-3.3.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/easymock/easymock/3.3.1
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/easymock/easymock/3.3.1/easymock-3.3.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/easymock/easymock-parent/3.3.1/easymock-parent-3.3.1.pom
/usr/share/java/.m2/repository/org/easymock/easymock/2.4/easymock-2.4.jar
/usr/share/java/.m2/repository/org/easymock/easymock/2.4/easymock-2.4.pom
/usr/share/java/.m2/repository/org/easymock/easymock/2.5.2/easymock-2.5.2.jar
/usr/share/java/.m2/repository/org/easymock/easymock/2.5.2/easymock-2.5.2.pom
/usr/share/java/.m2/repository/org/easymock/easymock/3.3.1/easymock-3.3.1.jar
/usr/share/java/.m2/repository/org/easymock/easymock/3.3.1/easymock-3.3.1.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-easymock/LICENSE.txt
/usr/share/package-licenses/mvn-easymock/src_site_License.html
