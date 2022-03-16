%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/galactic/.*$
%global __requires_exclude_from ^/opt/ros/galactic/.*$

Name:           ros-galactic-rqt-robot-monitor
Version:        1.0.5
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rqt_robot_monitor package

License:        BSD
URL:            http://wiki.ros.org/rqt_robot_monitor
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-rospkg
Requires:       ros-galactic-diagnostic-msgs
Requires:       ros-galactic-python-qt-binding >= 0.2.19
Requires:       ros-galactic-qt-gui
Requires:       ros-galactic-qt-gui-py-common
Requires:       ros-galactic-rclpy
Requires:       ros-galactic-rqt-gui
Requires:       ros-galactic-rqt-gui-py
Requires:       ros-galactic-rqt-py-common
Requires:       ros-galactic-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-galactic-ros-workspace
BuildRequires:  ros-galactic-rosidl-default-generators
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
rqt_robot_monitor displays diagnostics_agg topics messages that are published by
diagnostic_aggregator. rqt_robot_monitor is a direct port to rqt of
robot_monitor. All diagnostics are fall into one of three tree panes depending
on the status of diagnostics (normal, warning, error/stale). Status are shown in
trees to represent their hierarchy. Worse status dominates the higher level
status. Ex. 'Computer' category has 3 sub devices. 2 are green but 1 is error.
Then 'Computer' becomes error. You can look at the detail of each status by
double-clicking the tree nodes. Currently re-usable API to other pkgs are not
explicitly provided.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/galactic"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/galactic

%changelog
* Wed Mar 16 2022 Aaron Blasdel <ablasdel@gmail.com> - 1.0.5-1
- Autogenerated by Bloom

* Tue Apr 20 2021 Aaron Blasdel <ablasdel@gmail.com> - 1.0.4-2
- Autogenerated by Bloom

* Mon Mar 08 2021 Aaron Blasdel <ablasdel@gmail.com> - 1.0.4-1
- Autogenerated by Bloom

