# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/home/sujee/AI Github/pacman"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/home/sujee/AI Github/pacman/build"

# Utility rule file for behavior_tree_editor_autogen.

# Include the progress variables for this target.
include bt_editor/CMakeFiles/behavior_tree_editor_autogen.dir/progress.make

bt_editor/CMakeFiles/behavior_tree_editor_autogen:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir="/home/sujee/AI Github/pacman/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Automatic MOC for target behavior_tree_editor"
	cd "/home/sujee/AI Github/pacman/build/bt_editor" && /usr/bin/cmake -E cmake_autogen "/home/sujee/AI Github/pacman/build/bt_editor/CMakeFiles/behavior_tree_editor_autogen.dir/AutogenInfo.json" ""

behavior_tree_editor_autogen: bt_editor/CMakeFiles/behavior_tree_editor_autogen
behavior_tree_editor_autogen: bt_editor/CMakeFiles/behavior_tree_editor_autogen.dir/build.make

.PHONY : behavior_tree_editor_autogen

# Rule to build all files generated by this target.
bt_editor/CMakeFiles/behavior_tree_editor_autogen.dir/build: behavior_tree_editor_autogen

.PHONY : bt_editor/CMakeFiles/behavior_tree_editor_autogen.dir/build

bt_editor/CMakeFiles/behavior_tree_editor_autogen.dir/clean:
	cd "/home/sujee/AI Github/pacman/build/bt_editor" && $(CMAKE_COMMAND) -P CMakeFiles/behavior_tree_editor_autogen.dir/cmake_clean.cmake
.PHONY : bt_editor/CMakeFiles/behavior_tree_editor_autogen.dir/clean

bt_editor/CMakeFiles/behavior_tree_editor_autogen.dir/depend:
	cd "/home/sujee/AI Github/pacman/build" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/home/sujee/AI Github/pacman" "/home/sujee/AI Github/pacman/bt_editor" "/home/sujee/AI Github/pacman/build" "/home/sujee/AI Github/pacman/build/bt_editor" "/home/sujee/AI Github/pacman/build/bt_editor/CMakeFiles/behavior_tree_editor_autogen.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : bt_editor/CMakeFiles/behavior_tree_editor_autogen.dir/depend

