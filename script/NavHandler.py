from nbformat import write


class TemplateFile():         
    TEMPLATE_PATH = "templates/navbar.html"
    HEADER_NAV = "<!-- NAVBAR START -->"
    FOOTER_NAV = "<!-- NAVBAR END -->"

    def __init__(self) -> None:
        
        self.template_path = self.TEMPLATE_PATH
        self.template = self.read_template()
        
    def read_template(self):
        with open(self.template_path, "r") as template:
            data_template = template.readlines()
        return data_template
        
class FileHandler(TemplateFile):
    BUG_REPORT = []
    FILE_REPORT = {}

    def __init__(self, input_file, output_file, file_name) -> None:
        super().__init__()
        self.file_name = file_name
        self.file_path = input_file        
        self.file_list = self.read_file()
        self.output_file = output_file
        self.start_nav = self.find_start()
        self.end_nav = self.find_end()
        self.sum_it()
        

    def read_file(self):
        with open (self.file_path, "r") as file: 
            return file.readlines()

    def find_start(self):
        for line in self.file_list:
            if self.HEADER_NAV in line:
                return self.file_list.index(line)
        else:
            return -1

    def find_end(self):
            for line in self.file_list:
                if self.FOOTER_NAV in line:
                    return self.file_list.index(line)
            else:
                return -1
                
    def check_for_bugs(self):
        """Checks the read and return True or False to go on with the Prog or abort it"""
        if self.start_nav == -1 or self.end_nav == -1:
            self.appendBUG()
            return False
        else:
            print('\nFile "{}" checked: True'.format(self.file_name))
            return True

    def appendBUG(self):
        print('\nSomething went wrong with: "{}"'.format(self.file_name))
        print('Check "bug_report.txt"\n')
        self.BUG_REPORT.append(self.file_name)
        with open("bug_report.txt", "w") as report:
            report.write("Files NOT changed cus a Problem in File:\n")
            for line in self.BUG_REPORT:
                report.writelines(f"{line}\n")
                
    def clear_list(self):
        for i in range(self.start_nav, self.end_nav+1):
            self.file_list.pop(self.start_nav)
        print("Lines erased:",self.end_nav-self.start_nav+1)
            
    def insert_template(self):
        for x in range(len(self.template)-1,0,-1):
            self.file_list.insert(self.start_nav, self.template[x])
        print("Lines added: {}".format(len(self.template)))
            
    def sum_it(self):
        if self.check_for_bugs():
            self.clear_list()
            self.insert_template()
            self.write_file()
    
    def write_file(self):
        with open(self.output_file, "w") as output: 
            output.writelines(self.file_list)
        
            
        
        
        