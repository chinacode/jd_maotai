import sys
import time
from config import global_config
from jdlogger import logger
from jd_mask_spider_requests import Jd_Mask_Spider

if __name__ == '__main__':
    a = """
1.预约商品
2.秒杀抢购商品 
    """
    print(a)
    try:
        start_tool = Jd_Mask_Spider()
        choice_function = input('选择功能:')
        if choice_function == '1':
            start_tool.login()
            start_tool.make_reserve()
        elif choice_function == '2':
            tryTimes = 0
            skill_count = global_config.getRaw('config', 'kill_count')
            kill_per_time = global_config.getRaw('config', 'kill_per_time')
            while True:
                tryTimes = tryTimes + 1
                logger.info("-------------------------------------->开始第{}次抢购<--------------------------------------".format(tryTimes))
                start_tool.request_seckill_url()
                start_tool.request_seckill_checkout_page()
                # 可能需要的链接
                # https://tak.jd.com/t/98DD1?_t=1611281236817
                start_tool.submit_seckill_order()
                time.sleep(kill_per_time)
            logger.info("-------------------------------------->完成了{}次抢购,你运气不好没办法<--------------------------------------".format(tryTimes))
        else:
            logger.error("没有此功能")
            sys.exit(1)
    except Exception as e:
        logger.error("error {}".format(e))
