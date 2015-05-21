Summary: NethServer configuration for Wordpress
Name: nethserver-wordpress
Version: 1.0.1
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: http://dev.nethserver.org/projects/nethforge/wiki/%{name}
BuildRequires: nethserver-devtools

AutoReq: no
Requires: nethserver-httpd, nethserver-mysql
Requires: wordpress

%description
NethServer configuration for wordpress

%prep
%setup

%post

%preun

%build
%{__mkdir_p} root/usr/share/wordpress/tmp
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

%{genfilelist} \
     --dir /usr/share/wordpress/tmp 'attr(0750,apache,apache)' \
   $RPM_BUILD_ROOT > e-smith-%{version}-filelist
echo "%doc COPYING" >> %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f e-smith-%{version}-filelist
%defattr(-,root,root)


%description
Nethserver rpm to setup mysql database and web link for wordpress weblog

%changelog
* Thu May 21 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- Upgrade to wordpress 4.2

* Tue Feb 24 2015 Davide Principi <davide.principi@nethesis.it> - 1.0.0-2
- A new contrib Nethserver-wordpress by Stephane de Labrusse -- NethForge #2943

* Sat Nov 01 2014 stephane de Labrusse <stephdl@de-labrusse.fr> 1.0.0-1.ns6
- First release to nethserver

* Wed Oct 15 2014 stephane de Labrusse <stephdl@de-labrusse.fr> 1.2-3.sme
- Thanks to Remi Collet for the help to resolve the 'bug' 
- define('DISALLOW_FILE_MODS', false); :)
- Added another default value to {wordpress}{Salt}

* Tue Sep 02 2014 stephane de Labrusse <stephdl@de-labrusse.fr> 1.2-2.sme
- corrected the lack of module MIME::Base64 [SME: 8548]
- corrected the new ownership of www on /etc/wordpress [SME: 8546]
- added templates.metadata to root,www 0640 on /etc/wordpress/wp-config.php
- changed db {wordpress}{phrase} to {wordpress}{Salt}
 
* Wed Jun 20 2014 stephane de Labrusse <stephdl@de-labrusse.fr> 1.2-1.sme
- initial release to sme9

* Tue Nov 5 2013 JP Pialasse <tests@pialasse.com> 1.0-13.sme
- added chown to allow plugin instalaltion and translation

* Tue Nov 5 2013 JP Pialasse <tests@pialasse.com> 1.0-12.sme
- error in config file  [SME: 7978]
- also added more configuration option
- added /usr/share/php/ in phpbasedir [SME: 7977]
- patch cleanup, createlinks added to spec

* Sun Oct 27 2013 JP Pialasse <tests@pialasse.com> 1.0-10.sme
- rewritten for epel version of wordpress
- added createlinks and conf-wordpress event
- start cleaning spec file
- modified php base dir


* Wed Sep 04 2013 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.0.5 
- add www:www permission on /opt/wordpress folder to allow automatic update by FTP

* Wed Jun 05 2013 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.0.4
- add a tmp folder in httpd.conf

* Mon Jun 03 2013 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.0-3
- backup html-folder, mysql-base, and config-file during erase and upgrade process

* Thu May 29 2013 Stephane de Labrusse <stephdl@de-labrusse.fr>
- require sme8 due to wordpress 3.5 needs php version > 5.2

* Sat Nov 29 2008 Stephen Noble <support@dungog.net> 1.0-2
- http alias 80opt removed

* Fri Jul 06 2007 Stephen Noble <support@dungog.net> 1.0-1
- http alias, auto setup, template wp-config.php 

* Mon Dec 11 2006 Stephen Noble <support@dungog.net>
- rpm %post events reordered, to enable clean install 
- [0.9-5]

* Thu Nov 9 2006 Stephen Noble <support@dungog.net>
- http alias corrected
- [0.9-4]

* Thu Nov 9 2006 Stephen Noble <support@dungog.net>
- http PublicAccess setting added
- [0.9-3]

* Thu May 4 2006 Stephen Noble <support@dungog.net>
- httpd fragment modified
- rpm doesn't change file permissions
- [0.9-2]

* Sun Apr 16 2006 Stephen Noble <support@dungog.net>
- initial release
- [0.9-1]
