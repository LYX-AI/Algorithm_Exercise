#YAML
'''
Node_Type       : SwiftOps Platform
NF_Type         : SwiftOps Apps
NF_Version_Name : SwiftOps_2.2.0
Operation_Type  : Health Check
Schedule_Type   : Auto
Type            : Task-YML

Steps:
  - Check BGF SCTP Status

Check BGF SCTP Status:
  - Connection: swiftops_platform_ssh
    Commands:
      - Name: Check BGF SCTP operationalState
        Description: Run CLI to check SCTP status on all BGF nodes
        Command: cat /home/test/zain/bgf_sctp_status.log
        Register: "{{cmd_output}}"
        Post-process: passed, result=check_bgf_sctp_status()
        OK_Condition: |-
          [[ '{{$passed}}' == 'True' ]]
        NOK_Continue: True
        NOK_Note: |-
          echo "{{$result}}"

'''
# {"nodeType": "SwiftOps Platform", "nfType": "SwiftOps Apps", "operationType": "Health Check", "scheduleType": "Common", "type": "Python"}
# -*- coding: UTF-8 -*-

import re


def check_bgf_sctp_status(process_context):
    logger = process_context.getLogger()
    cmd_output = process_context.getCmdOutput()

    if not cmd_output or len(cmd_output) <= 1:
        logger.info("No valid cmd_output.")
        return False, "没有获取到有效输出"

    lines = cmd_output[1:]  # skip header
    failed_lines = []

    for line in lines:
        logger.info(f"[检查行]：{line}")
        match = re.search(r'operationalState:\s*(\w+)', line)
        if not match:
            logger.info("没有匹配到 operationalState 字段")
            failed_lines.append(f"未匹配: {line}")
        elif match.group(1) != "ENABLED":
            logger.info(f"状态异常: {match.group(1)}")
            failed_lines.append(f"异常状态: {line}")

    if failed_lines:
        return False, "\n".join(failed_lines)
    else:
        return True, "所有BGF节点状态为 ENABLED"

