# Nothing to strip in upstream binaries.
%define debug_package %{nil}

Name:           jad
Version:        1.5.8e
Release:        13%{?dist}
Summary:        Java Decompiler
License:        Distributable, free for non-commercial use
Group:          Development/Languages
URL:            http://www.kpdus.com/jad.html
Source:         http://www.kpdus.com/jad/linux/jadlx158.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:         %{_prefix}

%if 0%{?fedora} > 11 || 0%{?rhel} >= 6
ExclusiveArch:  i686
%else
ExclusiveArch:  i386
%endif


%description
A Java decompiler.


%prep
%setup -q -c
chmod 644 Readme.txt


%build
# Nothing to do.


%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 jad $RPM_BUILD_ROOT%{_bindir}/jad


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Readme.txt
%{_bindir}/jad


%changelog
* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.5.8e-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 25 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.5.8e-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.5.8e-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.5.8e-10
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.5.8e-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
- Fix default arch

* Sun Mar 29 2009 Julian Sikorski <belegdol@fedoraproject.org> - 1.5.8e-8
- Fedora 11 is i586, not i386

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.5.8e-7
- rebuild for new F11 features

* Thu Jul 24 2008 Conrad Meyer <konrad@tylerc.org> - 1.5.8e-6
- Initial import into RPM Fusion.

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.5.8e-5
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 19 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.5.8e-4
- Don't use BuildArch: i386, non-i386 buildsys can't make srpm out of it.

* Tue Sep 19 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.5.8e-3
- Update URLs, move "e" to version field.

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field
- drop Epoch

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Fri Jun 17 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:1.5.8-0.lvn.2.e
- Use dynamically linked upstream binary.

* Tue Nov 18 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.5.8-0.lvn.1.e
- Livnafied.

* Mon Oct 20 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.5.8-0.fdr.1
- Fedorafied.

* Thu Jul 31 2003 Bernhard Rosenkraenzer <bero@arklinux.org> 1.5.8-1ark
- initial RPM
