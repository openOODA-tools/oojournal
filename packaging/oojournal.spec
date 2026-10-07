Name:           oojournal
Version:        0.1.0
Release:        1%{?dist}
Summary:        Filters systemd journald logs by unit, slice, priority, and boot identifier.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oojournal
Source0:        oojournal-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oojournal is a sovereign, capability-bounded SYSTEMD JOURNAL written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oojournal
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oojournal-uninstall

%files
/usr/bin/oojournal
/usr/bin/oojournal-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
