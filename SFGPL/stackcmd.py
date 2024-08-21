class StackCMD():
    result_str_config_defalut={
        "func":"func",
        "before_cmd":"",
        "end_cmd":"",
        "begin":"(",
        "end":")",
        "split":",",
        "word_begin":"\"",
        "word_end":"\"",
        "zero_args_begin_and_end_flag":True,
    }

    @staticmethod
    def stackCMD(cmdlist:dict,cmdline:str,result_str_config:dict={},splitstr:str=" "):
        for key in StackCMD.result_str_config_defalut:
            result_str_config.setdefault(key,StackCMD.result_str_config_defalut[key])

        l=cmdline.split(splitstr)
        pycmd=StackCMD._stackCMDFunc(cmdlist=cmdlist,cmdline_list=l,cmd_stack_list=[],result_str="",result_str_config=result_str_config)
        return pycmd

    @staticmethod
    def _stackCMDFunc(cmdlist:dict,cmdline_list:list,cmd_stack_list:list,result_str:str,result_str_config:dict):
        if(len(cmdline_list)>0):
            head_s=cmdline_list[0]

            #read command name
            if(head_s in cmdlist):
                cmd_info=cmdlist[head_s]
                cmd_block=result_str_config["before_cmd"]+cmd_info[result_str_config["func"]]+result_str_config["end_cmd"]

                if(cmd_info["arg"]>0):
                    cmdsli={
                        "args":[],
                        "arg_n":0,
                        "info":cmd_info
                    }
                    cmd_stack_list.append(cmdsli)
                    result_str+=cmd_block+result_str_config["begin"]
                    return StackCMD._stackCMDFunc(cmdlist,cmdline_list[1:],cmd_stack_list,result_str,result_str_config)
                elif(cmd_info["arg"]==0):
                    result_str+=cmd_block
                    if(result_str_config["zero_args_begin_and_end_flag"]):
                        result_str+=result_str_config["begin"]+result_str_config["end"]
                    
                    nowcmd=cmd_stack_list[-1]
                    nowcmd["args"].append(head_s)
                    nowcmd["arg_n"]+=1
                    nowcmd,result_str,result_str_config,cmd_stack_list=StackCMD._endString(nowcmd,result_str,result_str_config,cmd_stack_list)
                    return StackCMD._stackCMDFunc(cmdlist,cmdline_list[1:],cmd_stack_list,result_str,result_str_config)

            else:
                #read command args
                if(len(cmd_stack_list)>0):
                    nowcmd=cmd_stack_list[-1]
                    if(nowcmd["arg_n"]<nowcmd["info"]["arg"]):
                        nowcmd["args"].append(head_s)
                        nowcmd["arg_n"]+=1
                        result_str+=result_str_config["word_begin"]+head_s+result_str_config["word_end"]

                        nowcmd,result_str,result_str_config,cmd_stack_list=StackCMD._endString(nowcmd,result_str,result_str_config,cmd_stack_list)
                    return StackCMD._stackCMDFunc(cmdlist,cmdline_list[1:],cmd_stack_list,result_str,result_str_config)
        else:
            return result_str
        
    @staticmethod
    def _endString(nowcmd,result_str,result_str_config,cmd_stack_list):
        while(nowcmd["arg_n"]==nowcmd["info"]["arg"]):
            result_str+=result_str_config["end"]
            cmd_stack_list=cmd_stack_list[:-1]
            if(len(cmd_stack_list)>0):
                nowcmd=cmd_stack_list[-1]
                nowcmd["arg_n"]+=1
            else:
                break
        if(nowcmd["arg_n"]!=nowcmd["info"]["arg"]):
            result_str+=result_str_config["split"]
        return nowcmd,result_str,result_str_config,cmd_stack_list
