import os
import Tools

def main():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    father_path=os.path.abspath(os.path.dirname(current_directory)+os.path.sep+".")

    table_list_path = current_directory + "\\create_table_message.txt"
    table_list = Tools.read_create_table_messages(table_list_path)

    Tools.write_c_t_m_file(table_list, father_path)

    kg_file_path_example = current_directory + "\\Database_kg.txt"
    kg_file_path_actual_1 = father_path + "\\Tree_Running\\Tree_Building\\Agents\\Tools\\Database_kg.txt"
    kg_file_path_actual_2 = father_path + "\\Tree_Running\\Agents\\Tools\\Database_kg.txt"
    Tools.write_kg_file(table_list, kg_file_path_example)
    Tools.write_kg_file(table_list, kg_file_path_actual_1)
    Tools.write_kg_file(table_list, kg_file_path_actual_2)

if __name__ == "__main__":
    main()