from castanett.core.support import *
import re
class HttpValidation:
    def __init__(self,args={},environ={}):
        self.args = args
        self.values = {}
        self.bool_validate = False
        self.method_type = ""
        self.environ = environ
        self.__init_method_exist();
    def is_validate_method_exist(self):

        return {"type":self.method_type,"status":self.bool_validate} #

    def get_values(self):

        return self.values
    def __init_method_exist(self):
        self.values = self.args
        self.values["sys_default"] = {}
        if self.args['method'] == "match":
            self.__execute_match()
            self.method_type  ="url"

        if self.args['method'] == "url":
            self.__execute_url()
            self.method_type  ="url"

        if self.args['method'] == "error":
            self.__execute_error()
            self.method_type  ="error"

    def __execute_match(self):
        url_match = re.match(self.args['routes'],self.__url_path_info(self.environ['PATH_INFO']))
        if url_match is not None:
            self.bool_validate = True

    def __execute_url(self):
        default_path = self.__url_path_info(self.environ['PATH_INFO']).split("/")
        segment_path = self.__url_path_info(self.args['routes']).split("/")
        bool_count = False
        local_var_ref = {}


        if default_path[0] == re.sub(r'\[(.*?)\]','',segment_path[0]):
            bool_count = True


        for k,v in enumerate(default_path):

            if len([sk for sk,sv in enumerate(segment_path) if sk==k ] )>0:
                segment_path_local = segment_path[k];
                if re.search(r'\[(.*?)\]',str(segment_path_local)):
                    segement_re_sub = re.sub("\[","",re.sub("\]","",segment_path_local))


                    review = self.__verify_url_action(segement_re_sub,v)
                    print(segment_path_local,"=",segement_re_sub,":s1",review)
                    if (review['is_valid']):
                        self.values["sys_default"][review['type']] = review['value']
                        local_var_ref[ review['type'] ]= review

                else:
                    review = self.__verify_url_action("action:"+(segment_path_local == "" and v or segment_path_local),v)

                    if (review['is_valid']):
                        local_var_ref[ review['type'] ]= review
                bool_count =   review['is_valid']
                if "action" not in local_var_ref and 'action' not in self.values["sys_default"] :
                    local_var_ref["action"]= review
            else:
                bool_count = False

        if bool_count:
            for jk,jv in local_var_ref.items():

                loc_is_valid = jv['is_valid']
                loc_type = jv['type']
                loc_value = jv['value']
                if loc_is_valid and loc_type not in self.values["sys_default"]:
                    self.values["sys_default"][loc_type ] = loc_value

        self.bool_validate = 'action' in self.values["sys_default"]
    def __execute_error(self):
        self.bool_validate = True


    def __url_path_info(self,loc_path_info):
        loc_path_info = re.sub(r'^/|/$','',loc_path_info)
        return loc_path_info

    def __verify_url_action(self,compare,value):
        bool_action = False;
        args = self.__url_argument(compare);

        action_split = (args['value'] ).split(",")


        if len(action_split) >=2:
            is_bool_valid_acton = False
            value_action = self.__convert_action_value("",args['type'])
            for ak,av in enumerate(action_split):
                if is_bool_valid_acton == False:
                    local_value =   self.__convert_action_value(av,args['type'])
                    if value == local_value:
                        bool_action = True
                        is_bool_valid_acton = True
                        value_action = value

        else:
            value_action =  self.__convert_action_value(value,args['type'])
            local_val = self.__convert_action_value(args['value'] =="-" and value_action or args['value'],args['type'])
            bool_action = value_action ==local_val
        return { "is_valid": bool_action,"type" : args['type'],"value" : value_action }

    def __url_argument(self,value):
        value_split = value.split(":")

        if len(value_split)>=2:
            action_segment_type= (value_split[0]).strip();
            action_segment_value= (value_split[1]).strip();
            return {"type":action_segment_type,"value":action_segment_value}
        else:
            action_segment_type= (value_split[0]).strip();
            return {"type":action_segment_type,"value":"-"}

    def __convert_action_value(self,value,types):
        value_action = ""

        if types == "action":
            if value in [""]:
                value_action = "index"
            else:
                value_action = value
        else:
            value_action = value

        return value_action

