# Mailcore2
## 发布的时候需要修改的宏定义
- MCAssert.c: MCDisabledAssert
- MCLog.c:  MCLogEnabled
## AbstractPart
- IMAPPart
- AbstractMessagePart:增加了header和mainPart
    - IMAPMessagePart:增加了size
- AbstractMultipart:增加parts()方法用来存放子part
    - IMAPMultipart
## 下载解析
(mailcore2)
    fetchMessages
(libetpan)
    mailimap_fetch
        mailimap_fetch_changedsince
            mailimap_fetch_qresync_vanished (在这里发送请求，并获取结果，判断的)
                mailimap_send_current_tag
                mailimap_fetch_send
                send_fetch_param
                mailimap_crlf_send
                mailstream_flush
                mailimap_parse_response
                    mailimap_parser_context_new
                    mailimap_response_parse_with_context/mailimap_response_parse
                        mailimap_response_parse_progress
                            mailimap_struct_multiple_parse_progress
                                parser(其实就是mailimap_cont_req_or_resp_data_parse_progress)
                                    (这里各种尝试)
                                    mailimap_continue_req_parse
                                        mailimap_star_parse
                                        mailimap_space_parse
                                        mailimap_resp_cond_state_parse
                                        mailimap_resp_cond_bye_parse
                                        mailimap_mailbox_data_parse
                                        mailimap_message_data_parse_progress
                                            mailimap_msg_att_parse_progress(重要，解析Header结构)
                                                mailimap_msg_att_new
                                                mailimap_struct_list_parse_progress(循环解析)
                                                    mailimap_msg_att_item_parse_progress
                                                        mailimap_msg_att_static_parse_progress
                                                            mailimap_msg_att_bodystructure_parse
                                                            mailimap_msg_att_body_parse
                                    mailimap_response_data_parse_progress
                                        mailimap_star_parse
                                        mailimap_resp_cond_state_parse
                                        mailimap_resp_cond_bye_parse
                                        mailimap_mailbox_data_parse
                                            mailimap_message_data_parse_progress（解析message）
                                                mailimap_msg_att_parse_progress
                                                    mailimap_struct_spaced_list_parse_progress
                                                        mailimap_struct_list_parse_progress（While 循环）
                                                            mailimap_msg_att_static_parse_progress
                                                                mailimap_msg_att_body_parse
                                                                mailimap_msg_att_bodystructure_parse
                                                                    mailimap_body_parse
                                                                        mailimap_body_type_1part_parse
                                                                            mailimap_body_type_msg_parse
                                                                            mailimap_body_type_text_parse
                                                                            mailimap_body_type_basic_parse
                                                                        mailimap_body_type_mpart_parse
                                                                            mailimap_struct_multiple_parse
                                                                mailimap_msg_att_body_section_parse_progress
                                        mailimap_capability_data_parse
                                        mailimap_extension_data_parse
                                        mailstream_log_error
                                        mailimap_crlf_parse
                                        (mailcore2)msg_att_handler


                                    mailimap_unstrict_char_parse
                                    mailimap_response_done_parse
                            mailimap_response_done_parse
                            mailimap_response_new
(mailcore2)
    msg_att_handler

## session
session->imap_response (response保存这里)
## 结构体
mailimap_response_info
mailimap_response
    clist rsp_cont_req_or_resp_data_list
    mailimap_response_done
        rsp_type
        (union)
            mailimap_response_tagged
                (char*)rsp_tag
                mailimap_resp_cond_state
                    rsp_type
                    mailimap_resp_text
                        mailimap_resp_text_code(这个结构体比较复杂，)
                            rc_type
                            (union)
                                clist * rc_badcharset
                                mailimap_capability_data
                                    clist * cap_list
                                clist * rc_perm_flags
                                rc_uidnext
                                rc_uidvalidity
                                rc_first_unseen
                                rc_atom
                                mailimap_extension_data
                                    mailimap_extension_api
                                        ext_name
                                        ext_id
                                    int ext_type;
                                    void * ext_data;
                        (char*)rsp_text
            mailimap_response_fatal
                mailimap_resp_cond_bye
                    mailimap_resp_text
                        mailimap_resp_text_code
                        char * rsp_text

## 5.29
读取一行
mailstream_read_line_append(fd, buffer)
