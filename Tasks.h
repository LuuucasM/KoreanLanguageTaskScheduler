#ifndef PRACTICE_TASKS_H
#define PRACTICE_TASKS_H

#include <string>
#include <ctime>
#include <map>
#include <vector>

/*The base class to all the different tasks.
Holds functions and attributes that all tasks have*/
class Task{
    protected:
        std::string _name;
        int _times_completed;
        int _times_to_do;
        int _chance;
    public:
        Task(std::string name, int times_completed, int times_to_do){
            _name = name;
            _times_completed = times_completed;
            _times_to_do = times_to_do;
        }

        virtual void do_task() {}
        
        inline int get_times_completed(){
            return _times_completed;
        }

        inline std::string get_name(){
            return _name;
        }

        inline void completed(){
            _times_completed++;
        }
};

class AnkiWords : public Task {
    public:
        AnkiWords(std::string name, int times_completed, int times_to_do) : Task(name, times_completed, times_to_do) {}

        virtual void do_task();

};

class AudioListen : public Task {
    protected:
        std::vector<std::string> sources;
        std::map<std::string, int> chapters;
    public:
        AudioListen(std::string name, int times_completed, int times_to_do) : Task(name, times_completed, times_to_do) {
            sources.push_back("ttmik easy reading beginner");
            chapters["ttmik easy reading beginner"] = 30;
        }
        
        virtual void do_task();

};

class GrammarGen : public Task {
    public:
        GrammarGen(std::string name, int times_completed, int times_to_do) : Task(name, times_completed, times_to_do) {}

        virtual void do_task();
};

class Journaling : public Task {
    public:
        Journaling(std::string name, int times_completed, int times_to_do) : Task(name, times_completed, times_to_do) {}

        virtual void do_task();
};

class KoreanNumbers : public Task {
    protected:
        std::map<char, std::string> sino_numbers = {
            {'0', "공"},
            {'1', "일"},
            {'2', "이"},
            {'3', "삼"},
            {'4', "사"},
            {'5', "오"},
            {'6', "육"},
            {'7', "칠"},
            {'8', "팔"},
            {'9', "구"}
        };
        std::map<int, std::string> sino_onefour = {
            {11, "백"},
            {10, "십"},
            {9, "억"},
            {8, "천"},
            {7, "백"},
            {6, "십"},
            {5, "만"},
            {4, "천"},
            {3, "백"},
            {2, "십"},
            {1, ""}
        };
        std::map<char, std::string> native_numbers = {
            {'0', "공"},
            {'1', "하나"},
            {'2', "둘"},
            {'3', "셋"},
            {'4', "넷"},
            {'5', "다섯"},
            {'6', "여섯"},
            {'7', "일곱"},
            {'8', "여덟"},
            {'9', "아홉"}
        };
        std::map<char, std::string> native_numbers_ten = {
            {'1', "열"},
            {'2', "스물"},
            {'3', "서른"},
            {'4', "마흔"},
            {'5', "쉰"},
            {'6', "에순"},
            {'7', "일흔"},
            {'8', "여든"},
            {'9', "아흔"}
        };
        std::string sino_to_string(std::string num);
        std::string native_to_string(std::string num);
    public:
        KoreanNumbers(std::string name, int times_completed, int times_to_do) : Task(name, times_completed, times_to_do) {}

        virtual void do_task();
};

class TextbookRead : public Task {
    public:
        TextbookRead(std::string name, int times_completed, int times_to_do) : Task(name, times_completed, times_to_do) {}

        virtual void do_task();
};

class SentenceMine : public Task {
    public:
        SentenceMine(std::string name, int times_completed, int times_to_do) : Task(name, times_completed, times_to_do) {}

        virtual void do_task();
};

#endif // PRACTICE_TASKS_H