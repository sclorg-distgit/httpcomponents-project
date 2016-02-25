%global pkg_name httpcomponents-project
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:              %{?scl_prefix}%{pkg_name}
Summary:           Common POM file for HttpComponents
Version:           6
Release:           4.11%{?dist}
License:           ASL 2.0
URL:               http://hc.apache.org/
# svn export http://svn.apache.org/repos/asf/httpcomponents/project/tags/%{version} %{pkg_name}-%{version}
# tar cJf %{pkg_name}-%{version}.tar.xz %{pkg_name}-%{version}
Source:            %{pkg_name}-%{version}.tar.xz
BuildArch:         noarch

BuildRequires:     %{?scl_prefix}maven-local


%description
Common Maven POM  file for HttpComponents. This project should be
required only for building dependant packages with Maven. Please don't
use it as runtime requirement.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :clirr-maven-plugin
%pom_remove_plugin :docbkx-maven-plugin
%pom_remove_plugin :maven-clover2-plugin
%pom_remove_plugin :maven-notice-plugin
%pom_xpath_remove pom:modules
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_file  : %{pkg_name}
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Feb 08 2016 Michal Srb <msrb@redhat.com> - 6-4.11
- Fix BR on maven-local & co.

* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 6-4.10
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 6-4.9
- maven33 rebuild

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 6-4.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 6-4.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 6-4.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 6-4.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 6-4.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 6-4.3
- Rebuild to fix incorrect auto-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 6-4.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 6-4.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 6-4
- Mass rebuild 2013-12-27

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
