#include "Tasks.h"

#include <Windows.h>

#include <fstream>
#include <iostream>
#include <random>
#include <algorithm>

#include "rapidjson/filereadstream.h"
#include "rapidjson/filewritestream.h"
#include "rapidjson/writer.h"
#include "rapidjson/document.h"

#define TODAYS_NUM_OF_TASKS 4
#define BUFF_SIZE 65536 //big number 2^16
#define NUM_OF_TASKS 6 //there are 6 tasks currently (not including ankiwords because i do that every day)

void gen_task_list(std::vector<Task *> *tasks, rapidjson::Document *d){
    for (rapidjson::Value::ConstMemberIterator m = d->MemberBegin(); m != d->MemberEnd(); ++m){
        if (m->name.GetString() == std::string("AudioListen")){
           tasks->push_back(new AudioListen(m->name.GetString(), m->value["times_completed"].GetInt(), m->value["times_to_do"].GetInt()));
        }
        else if (m->name.GetString() == std::string("GrammarGen")){
           tasks->push_back(new GrammarGen(m->name.GetString(), m->value["times_completed"].GetInt(), m->value["times_to_do"].GetInt()));
        }
        else if (m->name.GetString() == std::string("Journaling")){
           tasks->push_back(new Journaling(m->name.GetString(), m->value["times_completed"].GetInt(), m->value["times_to_do"].GetInt()));
        }
        else if (m->name.GetString() == std::string("KoreanNumbers")){
           tasks->push_back(new KoreanNumbers(m->name.GetString(), m->value["times_completed"].GetInt(), m->value["times_to_do"].GetInt()));
        }
        else if (m->name.GetString() == std::string("TextbookRead")){
           tasks->push_back(new TextbookRead(m->name.GetString(), m->value["times_completed"].GetInt(), m->value["times_to_do"].GetInt()));
        }
        else if (m->name.GetString() == std::string("SentenceMine")){
            tasks->push_back(new SentenceMine(m->name.GetString(), m->value["times_completed"].GetInt(), m->value["times_to_do"].GetInt()));
        }
    }
}



int main(){
    SetConsoleOutputCP(65001); //since this program will print korean letters make sure console doesnt print garbage

    //read from task data to generate a list of all the different tasks
    FILE *fp = fopen("task_data.json", "rb");
    char readBuffer[BUFF_SIZE];
    rapidjson::FileReadStream is(fp, readBuffer, sizeof(readBuffer));
    rapidjson::Document d;
    d.ParseStream(is);
    fclose(fp);
    std::vector<Task *> tasks;
    gen_task_list(&tasks, &d);

    //add the number of times each other task has been completed together
    //and when we randomly choose we are just going to choose the task
    //who has that range of number
    //this is to hopefully make sure that even though we are randomly choosing
    //tasks it will stay sortof uniform over time
    int percents[NUM_OF_TASKS];
    int total;
    for (int i = 0; i < tasks.size(); i++){
        for (int j = 0; j < (sizeof(percents)/sizeof(percents[0])); j++){
            if (j != i){
                percents[j] += tasks.at(i)->get_times_completed();
                total += tasks.at(i)->get_times_completed();
            }
        }
    }

    std::minstd_rand generator{(unsigned int)time(NULL)};
    int choice;

    //get todays tasks
    std::vector<Task *> todays_tasks;
    todays_tasks.push_back(new AnkiWords("AnkiWords", 1, 1)); // always do anki words every day :muscle:
    int counter;
    std::vector<int> chosen_ones;
    while (todays_tasks.size() < TODAYS_NUM_OF_TASKS){
        std::uniform_int_distribution<int> task_distr(0, total);
        choice = task_distr(generator);
        counter = 0;
        for (int i = 0; i < (sizeof(percents)/sizeof(percents[0])); i++){
            counter += percents[i];
            if (choice <= counter){
                if (std::find(todays_tasks.begin(), todays_tasks.end(), tasks.at(i)) == todays_tasks.end()){
                    todays_tasks.push_back(tasks.at(i));
                }
                break;
            }
        }
    }

    //this is the main while loop that the you interact with
    //loops until all tasks are complete
    while (todays_tasks.size() > 0){
        std::cout << "==============================" << std::endl;
        std::cout << "TODAYS TASK LIST: " << std::endl;
        std::cout << "==============================" << std::endl;
        for (int i = 0; i < todays_tasks.size(); i++){
            std::cout << i << ": " << todays_tasks.at(i)->get_name() << std::endl;
        }
        std::cout << "choose a task by inputting the corresponding number" << std::endl;
        std::cin >> choice;
        int ret_val;
        if (choice < todays_tasks.size()){
            todays_tasks.at(choice)->do_task();
            todays_tasks.at(choice)->completed();
            todays_tasks.erase(todays_tasks.begin()+choice);
        }
    }

    //save back the json data
    for (auto task : tasks){
        d[task->get_name().c_str()]["times_completed"] = task->get_times_completed();
    }

    fp = fopen("task_data.json", "wb");
    char writebuffer[BUFF_SIZE];
    rapidjson::FileWriteStream os(fp, writebuffer, sizeof(writebuffer));

    rapidjson::Writer<rapidjson::FileWriteStream> writer(os);
    d.Accept(writer);
    fclose(fp);
    return 0;
}