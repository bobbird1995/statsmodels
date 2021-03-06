# DO NOT EDIT
# Autogenerated from the notebook plots_boxplots.ipynb.
# Edit the notebook and then sync the output with this file.
#
# flake8: noqa
# DO NOT EDIT

#!/usr/bin/env python
# coding: utf-8

# # 箱线图

# 以下说明在 statsmodels 中的箱线图的一些选项。包括 `violin_plot` 和 `bean_plot`.

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# ## Bean 图

# 以下示例来自 `beanplot` 的文档
#
# 我们使用1996年美国全国选举调查数据集

# 确认受访者为自变量，年龄（除其他数据外）为因变量。

data = sm.datasets.anes96.load_pandas()
party_ID = np.arange(7)
labels = [
    "Strong Democrat", "Weak Democrat", "Independent-Democrat",
    "Independent-Independent", "Independent-Republican", "Weak Republican",
    "Strong Republican"
]

# 以 party ID 对年龄分组，并创建小提琴图:

plt.rcParams['figure.subplot.bottom'] = 0.23  # 设置标签可见
plt.rcParams['figure.figsize'] = (10.0, 8.0)  # 设置图形的大小
age = [data.exog['age'][data.endog == id] for id in party_ID]
fig = plt.figure()
ax = fig.add_subplot(111)
plot_opts = {
    'cutoff_val': 5,
    'cutoff_type': 'abs',
    'label_fontsize': 'small',
    'label_rotation': 30
}
sm.graphics.beanplot(age, ax=ax, labels=labels, plot_opts=plot_opts)
ax.set_xlabel("Party identification of respondent.")
ax.set_ylabel("Age")
#plt.show()


def beanplot(data, plot_opts={}, jitter=False):
    """helper function to try out different plot options
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plot_opts_ = {
        'cutoff_val': 5,
        'cutoff_type': 'abs',
        'label_fontsize': 'small',
        'label_rotation': 30
    }
    plot_opts_.update(plot_opts)
    sm.graphics.beanplot(data,
                         ax=ax,
                         labels=labels,
                         jitter=jitter,
                         plot_opts=plot_opts_)
    ax.set_xlabel("Party identification of respondent.")
    ax.set_ylabel("Age")


fig = beanplot(age, jitter=True)

fig = beanplot(age, plot_opts={'violin_width': 0.5, 'violin_fc': '#66c2a5'})

fig = beanplot(age, plot_opts={'violin_fc': '#66c2a5'})

fig = beanplot(age,
               plot_opts={
                   'bean_size': 0.2,
                   'violin_width': 0.75,
                   'violin_fc': '#66c2a5'
               })

fig = beanplot(age, jitter=True, plot_opts={'violin_fc': '#66c2a5'})

fig = beanplot(age,
               jitter=True,
               plot_opts={
                   'violin_width': 0.5,
                   'violin_fc': '#66c2a5'
               })

# ## 高级箱线图

# 基于示例脚本 `example_enhanced_boxplots.py` (Ralf Gommers 撰写)

import numpy as np
import matplotlib.pyplot as plt

import statsmodels.api as sm

# 水平轴标签
plt.rcParams['figure.subplot.bottom'] = 0.23

data = sm.datasets.anes96.load_pandas()
party_ID = np.arange(7)
labels = [
    "Strong Democrat", "Weak Democrat", "Independent-Democrat",
    "Independent-Independent", "Independent-Republican", "Weak Republican",
    "Strong Republican"
]

# 以 party ID 对年龄分组
age = [data.exog['age'][data.endog == id] for id in party_ID]

# 创建小提琴图.
fig = plt.figure()
ax = fig.add_subplot(111)

sm.graphics.violinplot(age,
                       ax=ax,
                       labels=labels,
                       plot_opts={
                           'cutoff_val': 5,
                           'cutoff_type': 'abs',
                           'label_fontsize': 'small',
                           'label_rotation': 30
                       })

ax.set_xlabel("Party identification of respondent.")
ax.set_ylabel("Age")
ax.set_title("US national election '96 - Age & Party Identification")

# Create a bean plot.
fig2 = plt.figure()
ax = fig2.add_subplot(111)

sm.graphics.beanplot(age,
                     ax=ax,
                     labels=labels,
                     plot_opts={
                         'cutoff_val': 5,
                         'cutoff_type': 'abs',
                         'label_fontsize': 'small',
                         'label_rotation': 30
                     })

ax.set_xlabel("Party identification of respondent.")
ax.set_ylabel("Age")
ax.set_title("US national election '96 - Age & Party Identification")

# 创建抖动图.
fig3 = plt.figure()
ax = fig3.add_subplot(111)

plot_opts = {
    'cutoff_val': 5,
    'cutoff_type': 'abs',
    'label_fontsize': 'small',
    'label_rotation': 30,
    'violin_fc': (0.8, 0.8, 0.8),
    'jitter_marker': '.',
    'jitter_marker_size': 3,
    'bean_color': '#FF6F00',
    'bean_mean_color': '#009D91'
}
sm.graphics.beanplot(age,
                     ax=ax,
                     labels=labels,
                     jitter=True,
                     plot_opts=plot_opts)

ax.set_xlabel("Party identification of respondent.")
ax.set_ylabel("Age")
ax.set_title("US national election '96 - Age & Party Identification")

# 创建非对称抖动图.
ix = data.exog['income'] < 16  # incomes < $30k
age = data.exog['age'][ix]
endog = data.endog[ix]
age_lower_income = [age[endog == id] for id in party_ID]

ix = data.exog['income'] >= 20  # incomes > $50k
age = data.exog['age'][ix]
endog = data.endog[ix]
age_higher_income = [age[endog == id] for id in party_ID]

fig = plt.figure()
ax = fig.add_subplot(111)

plot_opts['violin_fc'] = (0.5, 0.5, 0.5)
plot_opts['bean_show_mean'] = False
plot_opts['bean_show_median'] = False
plot_opts['bean_legend_text'] = 'Income < \$30k'
plot_opts['cutoff_val'] = 10
sm.graphics.beanplot(age_lower_income,
                     ax=ax,
                     labels=labels,
                     side='left',
                     jitter=True,
                     plot_opts=plot_opts)
plot_opts['violin_fc'] = (0.7, 0.7, 0.7)
plot_opts['bean_color'] = '#009D91'
plot_opts['bean_legend_text'] = 'Income > \$50k'
sm.graphics.beanplot(age_higher_income,
                     ax=ax,
                     labels=labels,
                     side='right',
                     jitter=True,
                     plot_opts=plot_opts)

ax.set_xlabel("Party identification of respondent.")
ax.set_ylabel("Age")
ax.set_title("US national election '96 - Age & Party Identification")

# 展示所有图.
#plt.show()
