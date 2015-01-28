set(LLVM_USED_LIBS clangTooling)

add_clang_executable(find-class-decls visitor.cpp)
