#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : acpica-unix2
Version  : 5.7.2022
Release  : 605
URL      : file:///aot/build/clearlinux/packages/acpica-unix2/acpica-unix2-v5.7.2022.tar.gz
Source0  : file:///aot/build/clearlinux/packages/acpica-unix2/acpica-unix2-v5.7.2022.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: acpica-unix2-bin = %{version}-%{release}
BuildRequires : bison
BuildRequires : flex
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-disable-Werror.patch

%description
No detailed description available

%package bin
Summary: bin components for the acpica-unix2 package.
Group: Binaries

%description bin
bin components for the acpica-unix2 package.


%prep
%setup -q -n acpica-unix2
cd %{_builddir}/acpica-unix2
%patch1 -p1

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1658320766
## altflags1f content
## altflags1
unset ASFLAGS
export CFLAGS="-DNDEBUG=1 -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=20 -march=skylake -mtune=skylake -mavx -mavx2 -msse2avx -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x4000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=20 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -Wno-inline"
export ASMFLAGS="-DNDEBUG=1 -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=20 -march=skylake -mtune=skylake -mavx -mavx2 -msse2avx -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x4000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=20 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -Wno-inline"
export CXXFLAGS="-DNDEBUG=1 -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=20 -march=skylake -mtune=skylake -mavx -mavx2 -msse2avx -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x4000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=20 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -Wno-inline"
export FCFLAGS="-DNDEBUG=1 -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=20 -march=skylake -mtune=skylake -mavx -mavx2 -msse2avx -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x4000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=20 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -Wno-inline"
export FFLAGS="-DNDEBUG=1 -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=20 -march=skylake -mtune=skylake -mavx -mavx2 -msse2avx -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x4000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=20 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -Wno-inline"
export LDFLAGS="-DNDEBUG=1 -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=20 -march=skylake -mtune=skylake -mavx -mavx2 -msse2avx -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x4000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=20 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -Wno-inline"
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
export MAKEFLAGS=%{?_smp_mflags}
%global _lto_cflags 1
%global _disable_maintainer_mode 1
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
export LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/glibc-hwcaps/x86-64-v3:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/glibc-hwcaps/x86-64-v3:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/local/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
export CPATH="/usr/local/cuda/include"
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH="/usr/share/defaults/fonts"
export GTK_IM_MODULE="xim"
export QT_IM_MODULE="cedilla"
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export NO_AT_BRIDGE=1
export GTK_A11Y=none
export PLASMA_USE_QT_SCALING=1
export QT_AUTO_SCREEN_SCALE_FACTOR=0
export QT_ENABLE_HIGHDPI_SCALING=0
export QT_FONT_DPI=88
export GTK_USE_PORTAL=1
export DESKTOP_SESSION=plasma
## altflags1f end
## make_macro content
make -j20
## make_macro end


%install
export SOURCE_DATE_EPOCH=1658320766
rm -rf %{buildroot}
## altflags1f content
## altflags1
unset ASFLAGS
export CFLAGS="-DNDEBUG=1 -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=20 -march=skylake -mtune=skylake -mavx -mavx2 -msse2avx -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x4000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=20 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -Wno-inline"
export ASMFLAGS="-DNDEBUG=1 -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=20 -march=skylake -mtune=skylake -mavx -mavx2 -msse2avx -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x4000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=20 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -Wno-inline"
export CXXFLAGS="-DNDEBUG=1 -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=20 -march=skylake -mtune=skylake -mavx -mavx2 -msse2avx -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x4000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=20 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -Wno-inline"
export FCFLAGS="-DNDEBUG=1 -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=20 -march=skylake -mtune=skylake -mavx -mavx2 -msse2avx -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x4000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=20 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -Wno-inline"
export FFLAGS="-DNDEBUG=1 -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=20 -march=skylake -mtune=skylake -mavx -mavx2 -msse2avx -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x4000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=20 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -Wno-inline"
export LDFLAGS="-DNDEBUG=1 -O3 -mno-vzeroupper --param=lto-max-streaming-parallelism=20 -march=skylake -mtune=skylake -mavx -mavx2 -msse2avx -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x4000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -funwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mrelax-cmpxchg-loop -feliminate-unused-debug-symbols -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=20 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fomit-frame-pointer -static-libstdc++ -static-libgcc -mrelax-cmpxchg-loop -pthread -Wl,--build-id=sha1 -Wno-inline"
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
export MAKEFLAGS=%{?_smp_mflags}
%global _lto_cflags 1
%global _disable_maintainer_mode 1
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
export LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/glibc-hwcaps/x86-64-v3:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/glibc-hwcaps/x86-64-v3:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/local/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
export CPATH="/usr/local/cuda/include"
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH="/usr/share/defaults/fonts"
export GTK_IM_MODULE="xim"
export QT_IM_MODULE="cedilla"
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export NO_AT_BRIDGE=1
export GTK_A11Y=none
export PLASMA_USE_QT_SCALING=1
export QT_AUTO_SCREEN_SCALE_FACTOR=0
export QT_ENABLE_HIGHDPI_SCALING=0
export QT_FONT_DPI=88
export GTK_USE_PORTAL=1
export DESKTOP_SESSION=plasma
## altflags1f end
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/acpibin
/usr/bin/acpidump
/usr/bin/acpiexamples
/usr/bin/acpiexec
/usr/bin/acpihelp
/usr/bin/acpisrc
/usr/bin/acpixtract
/usr/bin/iasl
