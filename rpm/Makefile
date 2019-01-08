NAME = nagios-plugins-weers
VERSION = $(shell cat version)
RPMDIR = ~/Dokumenty/projects/rpmy
REPLACE = ./string_replace.py
DISTRO = epel-7-x86_64
RELEASE = $(shell cat release)
MOCKDIR = /var/lib/mock

all: ver

ver:
	$(REPLACE) $(NAME).spec.in version $(VERSION) release $(RELEASE)

dist:
	rm -rf /tmp/$(NAME)-$(VERSION)
	mkdir -p /tmp/$(NAME)-$(VERSION)
	install -m 644 $(NAME).spec /tmp/$(NAME)-$(VERSION)
	install -m 644 ../check* /tmp/$(NAME)-$(VERSION)
	tar cjf /tmp/$(NAME)-$(VERSION).tar.bz2 -C /tmp $(NAME)-$(VERSION)
	mv /tmp/$(NAME)-$(VERSION).tar.bz2 $(RPMDIR)/SOURCES

rpm: dist
	rpmbuild -tb $(RPMDIR)/SOURCES/$(NAME)-$(VERSION).tar.bz2

srpm: dist
	rpmbuild -ts $(RPMDIR)/SOURCES/$(NAME)-$(VERSION).tar.bz2

mock: srpm
	mock --rebuild -r $(DISTRO) $(RPMDIR)/SRPMS/$(NAME)-$(VERSION)-$(RELEASE).fc`lsb_release -r -s`.src.rpm
