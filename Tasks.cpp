/*
This file implements the do_task() function of each of the different classes
*/
#include "Tasks.h"

#include <math.h>

#include <string>
#include <ctime>
#include <iostream>
#include <random>

void AnkiWords::do_task(){
    std::string user_input;
    int times = _times_to_do;
    while (times > 0){
        std::cout << "----------------------------" << std::endl;
        std::cout << "Starting Task: Anki Words " << times << " out of " << _times_to_do << std::endl;
        std::cout << "----------------------------" << std::endl;
        std::cout << "type 'done' when completed" << std::endl;
        std::cin >> user_input;
        std::cout << "are you really complete?" << std::endl;
        std::cin >> user_input;
        times--;
    }
}

void AudioListen::do_task(){
    int times = _times_to_do;
    std::string user_input;
    std::minstd_rand generator((unsigned int)time(NULL));
    std::uniform_int_distribution<int> source_distr(0, sources.size()-1);
    while (times > 0){
        std::cout << "----------------------------" << std::endl;
        std::cout << "Next up: Audio Listen" << times << " out of " << _times_to_do  << std::endl;
        std::cout << "----------------------------" << std::endl;
        int the_source = source_distr(generator);
        std::uniform_int_distribution<int> chapter_distr(1, chapters[sources.at(the_source)]);
        int the_chapter = chapter_distr(generator);
        std::cout << "you get " << sources.at(the_source) << "chapter: " << the_chapter << std::endl;
        std::cout << "type 'done' when the task is completed" << std::endl;
        std::cin >> user_input;
        std::cout << "are you sure you are done?" << std::endl;
        std::cin >> user_input;
        times--;
    }  
}

void GrammarGen::do_task(){
    int times = _times_to_do;
    std::string temp_string = std::to_string(times);
    std::string execute = "python3 grammar_gen.py " + temp_string;
    system(execute.c_str());
}

void Journaling::do_task(){
    std::string user_input;
    int times = _times_to_do;
    while (times > 0){
        std::cout << "----------------------------" << std::endl;
        std::cout << "Next up: Journaling" << times << " out of " << _times_to_do << std::endl;
        std::cout << "----------------------------" << std::endl;
        std::cout << "type 'done' when the task is completed" << std::endl;
        std::cin >> user_input;
        std::cout << "are you sure you are done?" << std::endl;
        std::cin >> user_input;
        times--;
    }
}


std::string KoreanNumbers::sino_to_string(std::string num){
    std::string first_num;
    std::string size_num;
    std::string final_string = "";
    while (num.size() > 0){
        first_num = sino_numbers[num[0]];
        size_num = sino_onefour[num.size()];
        if (num.size() == 1){
            if (final_string == "" || num != "0"){
                final_string += sino_numbers[num[0]];
            }
        }
        else if (num.size() == 5){
            if ((int)num[0] > 0){
                if (final_string == "" && (int)num[0] == 1){
                    final_string += size_num;
                }
                else{
                    final_string += first_num + size_num;
                }
            }
            else{
                final_string += size_num;
            }
        }
        else if (num.size() == 9){
            if ((int)num[0] > 0){
                final_string += first_num + size_num;
            }
            else{
                final_string += size_num;
            }
        }
        else{
            if (num[0] != '0' && num[0] != '1'){
                final_string += first_num + size_num;
            }
            if (num[0] == '1'){
                final_string += size_num;
            }
        }
        num.erase(0, 1);
    }
    return final_string;
}
std::string KoreanNumbers::native_to_string(std::string num){
    std::string final_string = "";
    if (num.size() == 1){
        final_string += native_numbers[num[0]];
    }
    else{
        final_string += native_numbers_ten[num[0]];
        if (num[1] != '0'){
            final_string += native_numbers[num[1]];
        }
    }
    return final_string;
}

void KoreanNumbers::do_task(){
    std::string user_input;
    std::minstd_rand generator((unsigned int)time(NULL));
    std::string number;
    std::string number_string;

    int times = _times_to_do;
    while (times > 0){
        std::cout << "----------------------------" << std::endl;
        std::cout << "Next up: Korean Numbers" << std::endl;
        std::cout << "----------------------------" << std::endl;
        std::uniform_int_distribution<int> sino_or_native(0, 1);
        int choice = sino_or_native(generator);
        if (choice == 0){
            std::cout << "convert this sino number" << std::endl;
            std::uniform_int_distribution<int> digits(0, 10);
            int num_digits = digits(generator);
            std::uniform_int_distribution<long int> the_number(pow(10, num_digits), (pow(10, (num_digits+1))-1));
            long int temp = the_number(generator);
            number = std::to_string(temp);
            number_string = sino_to_string(number);
        }
        else{
            std::cout << "convert this native number" << std::endl;
            std::uniform_int_distribution<int> the_number(0, 99);
            int temp = the_number(generator);
            number = std::to_string(temp);
            number_string = native_to_string(number);
        }
        std::uniform_int_distribution<int> num_or_str(0, 1);
        choice = num_or_str(generator);
        if (choice == 0){
            std::cout << "the number is: " << number << std::endl;
        }
        else{
            std::cout << "the number is: " << number_string << std::endl;
        }
        std::cout << "type 'done' to reveal the answer" << std::endl;
        std::cin >> user_input;
        std::cout << "are you sure your finished?" << std::endl;
        std::cin >> user_input;
        if (choice == 0){
            std::cout << number_string << std::endl;
        }
        else{
            std::cout << number << std::endl;
        }
        times--;
    }
}

void TextbookRead::do_task(){
    std::string user_input;
    int times = _times_to_do;
    while (times > 0){
        std::cout << "----------------------------" << std::endl;
        std::cout << "Next up: Textbook Read" << times << " out of " << _times_to_do << std::endl;
        std::cout << "----------------------------" << std::endl;
        std::cout << "enter 'done' when the task is complete" << std::endl;
        std::cin >> user_input;
        std::cout << "are you sure you are finished?" << std::endl;
        std::cin >> user_input;
        times--;
    }
}

void SentenceMine::do_task(){
    std::string user_input;
    int times = _times_to_do;
    while (times > 0){
        std::cout << "----------------------------" << std::endl;
        std::cout << "Next up: Sentence Mine" << times << " out of " << _times_to_do << std::endl;
        std::cout << "----------------------------" << std::endl;
        std::cout << "enter 'done' when the task is complete" << std::endl;
        std::cin >> user_input;
        std::cout << "are you sure you are finished?" << std::endl;
        std::cin >> user_input;
        times--;
    }
}