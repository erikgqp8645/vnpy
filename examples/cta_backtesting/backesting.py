from vnpy.app.cta_strategy.backtesting import BacktestingEngine, OptimizationSetting

from datetime import datetime
from examples.cta_backtesting.turtle_strategy import TurtleStrategy
# from backtesting_yue import BacktestingEngine,OptimizationSetting
engine = BacktestingEngine()
engine.set_parameters(
    vt_symbol="BTCUSD.BITFINEX",
    interval="1m",
    start=datetime(2019, 1, 1),
    end=datetime(2019, 10, 1),
    rate=0.3 / 1000,
    slippage=0.2,
    size=1,
    pricetick=0.2,
    capital=1000,
)
engine.add_strategy(TurtleStrategy, {})

engine.load_data()
engine.run_backtesting()
df = engine.calculate_result()
engine.calculate_statistics()
engine.show_chart()
exit()

setting = OptimizationSetting()
setting.set_target("sharpe_ratio")
setting.add_parameter("entry_window", 10, 1000, 100)
setting.add_parameter("exit_window", 10, 1000, 100)
setting.add_parameter("atr_window", 10, 1000, 100)

engine.run_ga_optimization(setting)