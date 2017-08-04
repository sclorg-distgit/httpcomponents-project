%{?scl:%scl_package httpcomponents-project}
%{!?scl:%global pkg_name %{name}}

Name:              %{?scl_prefix}httpcomponents-project
Summary:           Common POM file for HttpComponents
Version:           7
Release:           5.2%{?dist}
Group:             Development/Libraries
License:           ASL 2.0
URL:               http://hc.apache.org/
# svn export http://svn.apache.org/repos/asf/httpcomponents/project/tags/%{version} %{pkg_name}-%{version}
# tar cJf %{pkg_name}-%{version}.tar.xz %{pkg_name}-%{version}
Source:            %{pkg_name}-%{version}.tar.xz
BuildArch:         noarch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(org.apache:apache:pom:)

%description
Common Maven POM  file for HttpComponents. This project should be
required only for building dependant packages with Maven. Please don't
use it as runtime requirement.

%prep
%setup -n %{pkg_name}-%{version} -q
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :clirr-maven-plugin
%pom_remove_plugin :docbkx-maven-plugin
%pom_remove_plugin :maven-clover2-plugin
%pom_remove_plugin :maven-notice-plugin
%pom_remove_plugin :maven-site-plugin

%build
%mvn_file  : %{pkg_name}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%changelog
* Thu Jun 22 2017 Michael Simacek <msimacek@redhat.com> - 7-5.2
- Mass rebuild 2017-06-22

* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 7-5.1
- Automated package import and SCL-ization

* Thu Feb 23 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 7-5
- Regenerate build-requires

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 7-1
- Update to upstream version 7

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 6-5
- Rebuild to regenerate Maven auto-requires

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 6-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 17 2013 Michal Srb <msrb@redhat.com> - 6-2
- Build with xmvn

* Mon Aug  6 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 6-1
- Update to upstream version 6

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Feb 17 2011 Alexander Kurtakov <akurtako@redhat.com> 4.1.1-3
- Require maven (version 3) now.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 4.1.1-1
- Initial version
