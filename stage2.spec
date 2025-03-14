subarch: amd64
version_stamp: live-gui-full
target: livecd-stage2
rel_type: default
profile: default/linux/amd64/23.0/desktop/gnome
snapshot_treeish: @TREEISH@
source_subpath: default/livecd-stage1-amd64-live-gui.tar.xz
portage_confdir: /var/tmp/catalyst/config

livecd/bootargs: nodhcp secureconsole
livecd/depclean: no
livecd/fstype: squashfs
livecd/iso: livegui-amd64-@TIMESTAMP@.iso
livecd/type: gentoo-release-livecd
livecd/volid: gentoo-amd64-livegui

livecd/fsscript: @REPO_DIR@/files/fsscript-stage2.sh
livecd/rcadd: udev|sysinit udev-mount|sysinit acpid|default dbus|default gpm|default NetworkManager|default elogind|boot
livecd/unmerge: net-misc/netifrc

livecd/empty:
	/var/db/repos
	/usr/src

boot/kernel: gentoo

boot/kernel/gentoo/distkernel: yes
boot/kernel/gentoo/dracut_args: --xz --no-hostonly -a dmsquash-live -a mdraid -o btrfs -o crypt -o i18n -o usrmount -o lunmask -o qemu -o qemu-net -o nvdimm -o multipath -i /lib/keymaps /lib/keymaps -I busybox
boot/kernel/gentoo/packages: --usepkg n sys-fs/zfs broadcom-sta