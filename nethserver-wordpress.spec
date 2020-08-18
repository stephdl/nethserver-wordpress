Summary: NethServer configuration for Wordpress
Name: nethserver-wordpress-AutoUpdater
Version: 1.1.11
Release: 2%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: http://dev.nethserver.org/projects/nethforge/wiki/%{name}
BuildRequires: nethserver-devtools

AutoReq: no
Requires: nethserver-httpd, nethserver-mysql
Requires: wordpress-AutoUpdater
Requires: nethserver-rh-php73-php-fpm, rh-php73-php-pdo
Requires: rh-php73-php-gd, sclo-php73-php-imap, rh-php73-php-mbstring
Requires: rh-php73-php-mysqlnd, rh-php73-php-pdo, nethserver-rh-php73-php-fpm
Requires: rh-php73-php-opcache, rh-php73-php-pecl-apcu
Conflicts: wordpress nethserver-wordpress
%description
NethServer configuration for wordpress

%prep
%setup

%post

%preun

%postun
if [ $1 == 0 ] ; then
  # Fix the issue of orphan template in rh-php73-php-fpm configuration
  /usr/bin/rm -rf  /etc/opt/rh/rh-php73/php-fpm.d/z_wordpress.conf
  /usr/bin/systemctl restart  rh-php73-php-fpm.service
  # clean httpd template
  /usr/bin/rm -f /etc/httpd/conf.d/zzz_wordpress.conf
  /usr/bin/rm -f /etc/httpd/conf.d/wordpress.conf
  /usr/bin/systemctl reload httpd
fi

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
%dir %{_nseventsdir}/%{name}-update

%description
Nethserver rpm to setup mysql database and web link for wordpress weblog

%changelog
* Sun Jul 05 2020 stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.11
- Remove http templates after rpm removal

* Tue Jun 23 2020 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.10-1.ns7
- Move to rh-php73-php-fpm

* Sun Oct 27 2019 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.9-1.ns7
- Conflict wordpress nethserver-wordpress
- Fix the issue of orphan template in rh-php73-php-fpm configuration

* Sat Sep 14 2019 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.8-1.ns7
- Use rh-php73 instead of default php54
- Use our fork wordpress-AutoUpdater
- Obsolete wordpress 

* Sat Jul 07 2018 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.7-1.ns7
- Redirect acme-challenge to https

* Thu Jun 05 2018 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.6-1.ns7
- Renamed apache configuration to zzz_wordpress.conf
- Corrected the default path to apache ssl certificate
- Removed the useless apache template.metadata

* Sun Sep 10 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.5-1.ns7
- Restart httpd service on trusted-network

* Sun May 28 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.4-1.ns7
- Fixed wrong property in default-virtualhost.inc
- template expansion of default-virtualhost.inc

* Wed Mar 29 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.3-1.ns7
- Template expansion on trusted-network

* Thu Mar 16 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.2-2.ns7
- Changed DocumentRoot to DomainName property

* Sat Mar 11 2017 stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.1-1.ns7
- Virtualhost implementation

* Sat Mar 11 2017 stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.0-1.ns7
- Initial release to ns7

* Tue May 19 2015 stephane de Labrusse <stephdl@de-labrusse.fr> 1.0.0-3.ns6
- Add 'allowoverride All'

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
