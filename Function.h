#ifndef FUNCTION_H
#define FUNCTION_H

#include <functional>
#include <iostream>

template<typename... Args>
class FunctionWrapper {
public:
    FunctionWrapper() = default;

    template<typename Func>
    FunctionWrapper(Func&& func) : func_(std::make_unique<FuncType<Func>>(std::forward<Func>(func))) {}

    void operator()(Args... args) {
        if (func_) {
            (*func_)(args...);
        } else {
            std::cerr << "Function not set." << std::endl;
        }
    }

private:
    template<typename Func>
    class FuncType;

    template<typename Ret, typename... FArgs>
    class FuncType<std::function<Ret(FArgs...)>> {
    public:
        FuncType(std::function<Ret(FArgs...)> func) : func_(func) {}
        void operator()(FArgs... args) { func_(args...); }
    private:
        std::function<Ret(FArgs...)> func_;
    };

    std::unique_ptr<FuncType<std::function<void(Args...)>>> func_;
};

#endif // FUNCTION_H
